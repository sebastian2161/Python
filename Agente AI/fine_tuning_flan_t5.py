# fine_tuning_flan_t5.py con flujo de corrección manual y entrenamiento incremental

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Seq2SeqTrainer, Seq2SeqTrainingArguments, DataCollatorForSeq2Seq
from datasets import Dataset, load_dataset
import torch
import json
import os

# Configuración del modelo base (puede ser uno fine-tuned previamente)
model_name = "google/flan-t5-base" #"google/flan-t5-xl" #"google/flan-t5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Archivo donde se almacenan las instrucciones corregidas
CORRECTIONS_FILE = "./correcciones.json"

# Crear archivo si no existe
if not os.path.exists(CORRECTIONS_FILE):
    with open(CORRECTIONS_FILE, "w") as f:
        json.dump([], f)

# Cargar datos corregidos manualmente
with open(CORRECTIONS_FILE, "r") as f:
    correction_data = json.load(f)

if not correction_data:
    print("⚠ No hay correcciones guardadas. Agrega ejemplos en 'correcciones.json' antes de entrenar.")
    exit()

# Crear dataset a partir de correcciones
instructions = [x["instruction"] for x in correction_data]
responses = [x["response"] for x in correction_data]

dataset = Dataset.from_dict({
    "instruction": instructions,
    "response": responses
})

# Preprocesamiento
MAX_LENGTH = 128

def preprocess(example):
    input_text = example["instruction"]
    target_text = example["response"]
    model_inputs = tokenizer(input_text, max_length=MAX_LENGTH, truncation=True, padding="max_length")
    labels = tokenizer(target_text, max_length=MAX_LENGTH, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

dataset = dataset.map(preprocess)

# Entrenamiento
training_args = Seq2SeqTrainingArguments(
    output_dir="flan-t5-finetuned",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_dir="logs",
    save_total_limit=1,
    save_strategy="epoch",
    #evaluation_strategy="no",
    logging_steps=10,
    fp16=torch.cuda.is_available()
)

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

# Iniciar fine-tuning
trainer.train()

# Guardar modelo ajustado
model.save_pretrained("./flan-t5-finetuned")
tokenizer.save_pretrained("./flan-t5-finetuned")
print("✅ Modelo actualizado con correcciones guardadas.")
