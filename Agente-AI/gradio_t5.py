# gradio_correccion_finetune.py
import gradio as gr
import json
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Cargar modelo fine-tuned local
model_path = "google/flan-t5-xl" #"flan-t5-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)

# Archivo de correcciones
CORRECTIONS_FILE = "correcciones.json"
if not os.path.exists(CORRECTIONS_FILE):
    with open(CORRECTIONS_FILE, "w") as f:
        json.dump([], f)

def generar_respuesta(prompt):
    salida = pipe(prompt)[0]['generated_text']
    return salida

def guardar_correccion(prompt, correccion):
    with open(CORRECTIONS_FILE, "r") as f:
        datos = json.load(f)
    datos.append({"instruction": prompt, "response": correccion})
    with open(CORRECTIONS_FILE, "w") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    return "✅ Corrección guardada."

def interfaz(prompt):
    respuesta = generar_respuesta(prompt)
    return respuesta, prompt, respuesta

def procesar_guardado(prompt, correccion):
    if correccion.strip() == "":
        return "⚠️ La corrección está vacía."
    return guardar_correccion(prompt, correccion)

with gr.Blocks() as demo:
    gr.Markdown("""# 🧠 Corrección y Fine-Tuning para Flan-T5

1. Escribe un prompt.
2. Observa la respuesta generada.
3. Si es necesario, corrígela.
4. Guarda la corrección para fine-tuning futuro.
""")

    with gr.Row():
        prompt = gr.Textbox(label="📝 Instrucción (Prompt)", lines=2)
        boton_generar = gr.Button("Generar Respuesta")

    salida = gr.Textbox(label="📎 Respuesta generada", lines=3)
    correccion = gr.Textbox(label="✍️ Corrección manual (si aplica)", lines=3)
    boton_guardar = gr.Button("Guardar corrección")
    estado = gr.Textbox(label="📌 Estado", interactive=False)

    boton_generar.click(fn=interfaz, inputs=prompt, outputs=[salida, prompt, correccion])
    boton_guardar.click(fn=procesar_guardado, inputs=[prompt, correccion], outputs=estado)

if __name__ == "__main__":
    demo.launch()
