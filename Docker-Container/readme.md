# 📡 Despliegue Automático de Contenedores Docker con Google Cloud  
## Cloud Run + Cloud Build + Artifact Registry

Este proyecto demuestra cómo implementar una arquitectura de **despliegue automático de contenedores Docker**, utilizando servicios completamente gestionados de Google Cloud Platform (GCP):

- 🚀 **Cloud Run (basado en Functions Framework)** para activar eventos mediante peticiones HTTP.
- 🔄 **Cloud Build**, para compilar automáticamente el contenedor Docker desde el código fuente.
- 📦 **Artifact Registry**, para almacenar de forma segura las imágenes Docker generadas.

---

## 🧱 Arquitectura General

1. El caso de uso implementado está basado en el siguiente repositorio de ejemplo:  
   👉 [services_trigger-function-Dataflow](https://github.com/sebastian2161/Python/blob/main/services_trigger-function-Dataflow/readme.md)

2. Una vez desplegada la función, **Cloud Build** compila automáticamente la imagen Docker y la almacena en:
   us-central1-docker.pkg.dev/[TU_PROYECTO]/cloud-run-source-deploy/[NOMBRE_DEL_SERVICIO].


3. La imagen Docker queda disponible en **Artifact Registry**, desde donde puede reutilizarse o desplegarse nuevamente con Cloud Run o Cloud Functions (2ª gen).

---

## 📦 Componentes del Proyecto

### 1. Cloud Run (basado en Functions Framework)

- **Archivo principal**: `main.py`  
- **Punto de entrada (entry point)**: `hello_http`  
- **Framework utilizado**: [Functions Framework for Python](https://cloud.google.com/functions/docs/functions-framework)  
- **Tipo de activación**: HTTP (`--trigger-http`)

---

### 2. Cloud Build

- Construye automáticamente la imagen Docker desde el código fuente.
- No se requiere escribir un `Dockerfile` ni ejecutar `docker build` manualmente.
- Se ejecuta automáticamente cuando se despliega el servicio desde Cloud Run con el parámetro `--source`.

---

### 3. Artifact Registry

- Almacena la imagen Docker generada por Cloud Build en: us-central1-docker.pkg.dev/[TU_PROYECTO]/cloud-run-source-deploy/[NOMBRE_DEL_SERVICIO]



- Las imágenes pueden reutilizarse para nuevos despliegues o visualizarse mediante el comando `gcloud artifacts`.

---

## ✅ Beneficios del Enfoque

- 🔄 **Despliegue automatizado** desde código fuente a contenedor.
- 💡 **Reutilización de imágenes** para distintos entornos (dev, test, prod).
- 🛡️ **Seguridad integrada** a través de IAM y control de acceso a Artifact Registry.
- 🧩 **Escalabilidad automática** con Cloud Run.

---

## 📁 Repositorio y Caso de Uso

Este proyecto se basa en el siguiente ejemplo real:  
🔗 [https://github.com/sebastian2161/Python/blob/main/services_trigger-function-Dataflow/readme.md](https://github.com/sebastian2161/Python/blob/main/services_trigger-function-Dataflow/readme.md)











