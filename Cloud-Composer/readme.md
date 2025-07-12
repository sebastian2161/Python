# 📡 Orquestación de Servicios con Google Cloud: Cloud Composer + Dataflow

Este proyecto demuestra cómo implementar una arquitectura de orquestación de workflows utilizando **Cloud Composer** (basado en **Apache Airflow**) para automatizar la ejecución de procesos en **Dataflow**.

---

## 🚀 Arquitectura General

1. Los archivos `.py` de los jobs de **Dataflow** son almacenados previamente en un bucket de **Cloud Storage**.
2. **Cloud Composer** ejecuta un DAG diariamente que activa dos tareas de forma secuencial:
   - **Tarea 1**: Ejecuta el primer job de Dataflow.
   - **Tarea 2**: Ejecuta el segundo job de Dataflow después de finalizar la primera.
3. Los resultados procesados se almacenan en un bucket de destino en **Cloud Storage**.

---

## 📦 Componentes del Proyecto

### 1. Servicio: Dataflow

- **Archivos**:
  - `composer_dataflow.py`
  - `composer_dataflow1.py`
- **Función**: Cada archivo representa un pipeline de Apache Beam que se ejecuta como un job de Dataflow para procesar datos de forma escalable.
- **Ubicación**: Estos archivos deben estar cargados previamente en un bucket GCS accesible por Cloud Composer.

### 2. Servicio: Cloud Composer (Apache Airflow)

- **Archivo**: `dag.py`
- **Función**: Define un DAG que ejecuta dos tareas `DataflowCreatePythonJobOperator` de forma secuencial.
- **Frecuencia**: El DAG está configurado para ejecutarse una vez al día (`schedule_interval=timedelta(days=1)`).

### 3. Servicio: Cloud Storage

- **Uso**:
  - **Staging y temp**: Requeridos por los jobs de Dataflow durante su ejecución.
  - **Results**: Los archivos de salida generados por los pipelines serán almacenados aquí.
- **Ruta de revisión**: Accede al bucket destino (por ejemplo: `gs://beam_dataflow_cl/results/`) para validar los resultados procesados.

---

## ✅ Requisitos Previos

1. Habilitar los siguientes servicios en GCP:
   - Cloud Composer
   - Dataflow
   - Cloud Storage

2. Asegurar que la cuenta de servicio usada por Composer tenga los siguientes permisos:

   - `roles/composer.worker`
   - `roles/dataflow.admin`
   - `roles/storage.admin`

---

## 🛠️ Cómo Ejecutar

1. Subir los archivos `composer_dataflow.py` y `composer_dataflow1.py` al bucket de Cloud Storage.
2. Subir el archivo `dag.py` a la carpeta `dags/` de tu entorno de Cloud Composer.
3. Verificar en la interfaz de **Airflow** que el DAG esté habilitado y programado.
4. Esperar la ejecución automática o disparar el DAG manualmente para probarlo.
5. Validar los resultados procesados en el bucket destino especificado.









