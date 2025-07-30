# 📡 Despliegue de Dataproc (Cluster Apache Hadoop con Apache Spark) en Vertex AI utilizando Google Cloud Platform (GCP)

Este proyecto demuestra cómo implementar una arquitectura **Big Data con Análisis Predictivo** para un pipeline PySpark en **Vertex AI**, utilizando **Dataproc**.

---

## 🚀 Arquitectura General

La solución tiene la siguiente arquitectura:

1. Crear un cluster (Hadoop con Spark) en el servicio **Dataproc**.
2. Crear una instancia Workbench en **Vertex AI**.
3. Configurar el ambiente con la librería `pyspark` y Java (OpenJDK) en Vertex AI.
4. Realizar pruebas de compatibilidad de Spark con Java.
5. Desarrollar un script PySpark para validar su funcionamiento local.
6. Ejecutar trabajos de Dataproc desde Vertex AI utilizando la herramienta `gcloud dataproc jobs`.

---

## 🧪 Componentes del Proyecto

### 1. Vertex AI Workbench - `Dataproc-pyspark.py` - `Dataproc-pyspark.ipynb`

- Código principal del pipeline que realiza análisis de Big Data.
- Ejecuta trabajos de Spark sobre Dataproc desde Vertex AI.

### 2. Dataproc - `Cluster Apache Hadoop con Apache Spark`

- Cluster gestionado que permite ejecutar tareas distribuidas de Spark.
- Compatible con librerías GCP como BigQuery, GCS, etc.

---

## ✅ Pre-requisitos

- Tener habilitados los siguientes servicios en GCP:
  - Vertex AI
  - Dataproc
  - Cloud Storage
  - Cloud Logging

- Configurar permisos adecuados para la cuenta de servicio:
  - `roles/dataproc.editor`
  - `roles/storage.objectViewer`

---

## ⚙️ Pasos para Desplegar el Proyecto

### 1. Crear Cluster en Dataproc

```bash
gcloud dataproc clusters create pyspark-cluster \
  --region=us-central1 \
  --zone=us-central1-c \
  --single-node \
  --master-machine-type=n1-standard-2 \
  --image-version=2.0-debian10 \
  --optional-components=JUPYTER \
  --enable-component-gateway
```

### 2. Crear instancia Vertex AI Workbench

- Desde la consola GCP, crear una instancia de Workbench.
- Tipo: "User-managed notebooks"
- Seleccionar imagen: `Deep Learning VM` o personalizada con `pyspark`.

### 3. Configurar entorno Vertex AI

Instala Java y PySpark:
```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
pip install pyspark --break-system-packages
```

Configura la variable `JAVA_HOME`:
```bash
export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
```

### 4. Crear archivo PySpark: `Dataproc-pyspark.py`

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("VertexAI-Dataproc").getOrCreate()

# Crear DataFrame
df = spark.createDataFrame([(1, 'Google'), (2, 'Cloud')], ["id", "name"])
df.show()

spark.stop()
```

### 5. Ejecutar PySpark en Dataproc desde Vertex AI

```bash
gcloud dataproc jobs submit pyspark Dataproc-pyspark.py \
  --cluster=pyspark-cluster \
  --region=us-central1
```

### 6. Verifica los resultados

- Accede a la consola GCP → Dataproc → Trabajos.
- Visualiza los logs y resultados del DataFrame.

---

## 📚 Recursos Adicionales

- [Dataproc en GCP](https://cloud.google.com/dataproc/docs)
- [Vertex AI Workbench](https://cloud.google.com/vertex-ai/docs/workbench)
- [PySpark API](https://spark.apache.org/docs/latest/api/python/)
- [Gcloud CLI - Dataproc](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark)

---

## 📢 Contacto

Autor: **Sebastian Collao**
Repositorio: [https://github.com/sebastian2161/Python]
