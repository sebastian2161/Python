# 📡 Despliegue de Pipeline CI/CD en Vertex AI utilizando Google Cloud Platform (GCP): Vertex AI + Cloud Storage + Cloud Build

Este proyecto demuestra cómo implementar una arquitectura de **CI/CD (Integración y Despliegue Continuo)** para un pipeline analítico/predictivo en **Vertex AI**, 
utilizando servicios nativos de **Google Cloud Platform** como **Cloud Storage** y **Cloud Build**.

---

## 🚀 Arquitectura General

La solución sigue la siguiente arquitectura:

1. El desarrollo del pipeline se realiza localmente o desde Vertex AI Workbench.
2. Al realizar un `git push` a una rama específica del repositorio en GitHub, se activa un **Trigger de Cloud Build**.
3. **Cloud Build** compila y ejecuta automáticamente el pipeline definido en el archivo `pipeline.py`.
4. El pipeline puede consumir datos desde un bucket en **Cloud Storage**.

---

## 🧱 Servicios Utilizados

| Servicio GCP       | Rol en la Arquitectura                                                                 |
|--------------------|----------------------------------------------------------------------------------------|
| **Vertex AI**      | Desarrollo del pipeline analítico/predictivo                                           |
| **Cloud Storage**  | Almacenamiento de datos fuente (e.g., `data.csv`) utilizados por el pipeline           |
| **Cloud Build**    | Ejecución automatizada del pipeline al realizar `push` en GitHub (CI/CD)               |

---

## 📁 Estructura del Repositorio

📦 vertex-ai-cicd
├── pipeline.py # Código del pipeline predictivo
├── requirements.txt # Dependencias Python necesarias
├── data.csv # Archivo de entrada almacenado en GCS
└── cloudbuild.yaml # Script de construcción para Cloud Build



---

## 🧪 Componentes del Proyecto

### 1. Vertex AI - `pipeline.py`

- Código principal del pipeline que realiza análisis o predicciones.
- Debe estar preparado para ejecutarse sin intervención manual (automatizable).

### 2. Cloud Storage - `data.csv`

- Contiene los datos de entrada del pipeline.
- Asegúrate de subir este archivo al bucket correspondiente y actualizar la ruta en el código.

### 3. Cloud Build - `cloudbuild.yaml`

- Orquestador que ejecuta el pipeline automáticamente.
- Se activa con un trigger al hacer `push` en la rama configurada de GitHub.



---

## ✅ Pre-requisitos

Asegúrate de cumplir con los siguientes pasos antes de ejecutar el pipeline:

### 🔌 Servicios habilitados en GCP

- [x] **Vertex AI**
- [x] **Cloud Build**
- [x] **Cloud Storage**
- [ ] **Artifact Registry** *(opcional, solo si usas imágenes personalizadas)*

### 📂 Cloud Storage

- [x] Crear un **bucket** en Cloud Storage.
- [x] Subir el archivo `data.csv` al bucket correspondiente.
- [x] Verifica que la ruta usada en el script `pipeline.py` apunte correctamente al archivo en el bucket.

### 🔁 Trigger de Cloud Build

- [x] Crear un **trigger de compilación** con las siguientes configuraciones:
  - **Tipo**: GitHub
  - **Evento**: Push a una rama específica (por ejemplo, `main`)
  - **Ubicación del archivo YAML**: Raíz del repositorio (`cloudbuild.yaml`)

### 🔐 Permisos de la cuenta de servicio (IAM)

Asegúrate de que la cuenta de servicio usada por **Cloud Build** tenga los siguientes roles asignados:

- `roles/storage.objectViewer` → Permite leer archivos del bucket
- `roles/aiplatform.user` → Permite ejecutar recursos en Vertex AI
- `roles/cloudbuild.builds.editor` → Permite ejecutar y gestionar builds

---

## 🚀 Ejecución

Una vez que todo está configurado correctamente, realiza lo siguiente:

### 1. Modifica tu archivo local

Haz cambios en `pipeline.py` o cualquier otro componente del proyecto.

### 2. Realiza un commit y push

```bash
git add .
git commit -m "Update pipeline"
git push origin main



---

## ✅ Resultado Esperado

Al ejecutar el `git push`, se espera lo siguiente:

- 🚀 Se activa el **trigger de Cloud Build** configurado previamente.
- 🧠 El archivo `pipeline.py` es ejecutado como parte del proceso de compilación en Vertex AI.
- ☁️ El pipeline consume el archivo `data.csv` directamente desde **Cloud Storage**.
- 🔍 Los resultados del pipeline estarán disponibles desde:
  - 📊 La consola de **Vertex AI**
  - 📁 Los registros en **Cloud Logging**
  - 📝 Cualquier salida definida dentro del script (`print()`, `logging`, etc.)

---




