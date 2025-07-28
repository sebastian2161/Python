# 📱 Despliegue de Aplicación Django/FastAPI/Flask como SaaS en Google Cloud Platform (GCP)

Este proyecto demuestra cómo desplegar una **aplicación web Django, FastAPI o Flask** bajo el modelo **SaaS (Software como Servicio)** utilizando **Cloud Run**, **Cloud Build** y **Artifact Registry** en GCP.

---

## 🚀 Arquitectura General

1. Crear el proyecto en Flask, FastAPI o Django.
2. Crear el archivo `requirements.txt`.
3. Crear el archivo `Dockerfile`.
4. Compilar la imagen Docker con Cloud Build.
5. Desplegar la imagen Docker en Cloud Run.

---

## 🧱️ Componentes del Proyecto

### ⚙️ Cloud Build

- Compila el `Dockerfile`, crea una imagen y la almacena en **Artifact Registry**.

### ⚙️ Artifact Registry

- Almacena la imagen Docker, la cual será utilizada por **Cloud Run**.

### ⚙️ Cloud Run

- Despliega la imagen Docker, crea un servicio accesible públicamente en una URL:

```
https://[NOMBRE_SERVICIO]-cloudrun-XXXXXX-REGION.run.app/
```

---

## ⚙️ Pasos para Desplegar la Aplicación Web **Django**

### 📂 Estructura del Proyecto Django
```
my_django_project/
├── Dockerfile
├── requirements.txt
├── manage.py
├── myapp/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py
└── my_django_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### 📋 Pasos:
1. Crear carpeta en Cloud Shell:
```bash
mkdir django-cloudrun && cd django-cloudrun
```
2. Crear el proyecto Django:
```bash
   subir la carpeta my_django_project a django-cloudrun de Cloud Shell.
```
3. Crear archivo `requirements.txt`:
```
Django==4.2
gunicorn==21.2.0
```
4. Crear archivo `Dockerfile`:
```Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "my_django_project.wsgi:application", "--bind", "0.0.0.0:8080"]
```
5. Compilar imagen Docker con Cloud Build:
```bash
gcloud builds submit --tag gcr.io/PROYECTO_ID/django-cloudrun
```
6. Desplegar imagen en Cloud Run:
```bash
gcloud run deploy django-cloudrun \
  --image gcr.io/PROYECTO_ID/django-cloudrun \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## ⚙️ Pasos para Desplegar la Aplicación Web **FastAPI**

### 📂 Estructura del Proyecto FastAPI
```
fastapi-cloudrun/
├── app.py
├── Dockerfile
└── requirements.txt
```

### 📋 Pasos:
1. Crear carpeta:
```bash
mkdir fastapi-cloudrun && cd fastapi-cloudrun
```
2. Crear archivo `app.py`:
```# app.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def hello():
    return "¡Hola Bienvenido a Cloud Run con FastAPI!"
```
3. Crear archivo `requirements.txt`:
```
fastapi
uvicorn[standard]
```
4. Crear archivo `Dockerfile`:
```Dockerfile
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia archivos de tu app al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto 8080 (requerido por Cloud Run)
EXPOSE 8080

# Comando de inicio para uvicorn (servidor FastAPI)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
```
5. Compilar imagen Docker:
```bash
gcloud builds submit --tag gcr.io/PROYECTO_ID/fastapi-cloudrun
```
6. Desplegar imagen en Cloud Run:
```bash
gcloud run deploy fastapi-cloudrun \
  --image gcr.io/PROYECTO_ID/fastapi-cloudrun \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## ⚙️ Pasos para Desplegar la Aplicación Web **Flask**

### 📂 Estructura del Proyecto Flask
```
flask-cloudrun/
├── app.py
├── Dockerfile
└── requirements.txt
```

### 📋 Pasos:
1. Crear carpeta:
```bash
mkdir flask-cloudrun && cd flask-cloudrun
```
2. Crear archivo `app.py`:
```# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Bienvenido a la App Flask en Google Cloud-GCP!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```
3. Crear archivo `requirements.txt`:
```
flask
```
4. Crear archivo `Dockerfile`:
```# Dockerfile
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Puerto usado por Cloud Run
ENV PORT=8080

# Comando para ejecutar la app
CMD ["python", "app.py"]
```
5. Compilar imagen Docker:
```bash
gcloud builds submit --tag gcr.io/PROYECTO_ID/flask-cloudrun
```
6. Desplegar imagen en Cloud Run:
```bash
gcloud run deploy flask-cloudrun \
  --image gcr.io/PROYECTO_ID/flask-cloudrun \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 📚 Recursos Adicionales

- [Flask Oficial](https://flask.palletsprojects.com/)
- [FastAPI Oficial](https://fastapi.tiangolo.com/)
- [Django Oficial](https://www.djangoproject.com/)
- [Cloud Run - Documentación](https://cloud.google.com/run/docs)
- [Cloud Build - Documentación](https://cloud.google.com/build/docs)
- [Artifact Registry - Documentación](https://cloud.google.com/artifact-registry/docs)
- [GCP CLI - gcloud](https://cloud.google.com/sdk/gcloud)

---

## 🚀 Autor

**Sebastián Collao**  | Proyecto SaaS

---
