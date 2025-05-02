# Agente Local con LangChain + Hugging Face

Este proyecto ejecuta un agente AI **completamente en local**, sin depender de OpenAI, utilizando LangChain y modelos de Hugging Face.

## 🧰 Requisitos

- Python 3.8+
- VS Code (opcional)
- Acceso a internet solo para descargar el modelo la primera vez

## 🚀 Instalación

1. Clona el proyecto o crea una carpeta `agente_local`
2. Crea entorno virtual:

    - bash
      - python -m venv venv
      - source venv/bin/activate    # Linux
      - .\venv\Scripts\activate     # Windows

    - Instalación de librerias
      - Ejecutar el pip install -r requirement.txt 


## 🚀 Ciclo de entrenamiento, despliegue  y mejora incremental del Agente AI utilizando el modelo google/flan-t5-base y google/flan-t5-xl.

1. Ejecutar el archivo fine_tuning_flan_t5.py, para realizar el entrenamiento de Agente AI utilizando el modelo google/flan-t5-base.

2. Terminado el entrenamiento del modelo, sera guardado en la carpeta flan-t5-finetuned.

3. El despliegue del Agente AI sera a través del gradio_t5.py, que creará un servidor web que se ejecutará en la url local: 127:0.0.1:7860
   con la interfaz web del Agente AI. 

5. Podrá realizar un entrenamiento incremental en el modelo google/flan-t5-base, corrigiendo las respuestas y guardandolas en el correcciones.json que será nuestro conjunto de datos de entrenamiento.

6. Ejecutar fine_tuning_flan_t5.py cada vez que tenga correcciones de respuestas, para entrenar y actualizar el modelo.

![Interfaz Web Agente AI](https://github.com/sebastian2161/Python/blob/main/Agente-AI/Interfaz_web_agente_AI.png?raw=true)


