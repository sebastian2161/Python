📡 Orquestación de Servicios con Google Cloud: Cloud Composer + Dataflow
Este proyecto demuestra cómo implementar una arquitectura de orquestación de workflows utilizando Cloud Composer (basado en Apache Airflow) para automatizar la ejecución de procesos de Dataflow.

🚀 Arquitectura General
Los archivos .py de los jobs de Dataflow son almacenados previamente en un bucket de Cloud Storage.

Cloud Composer (DAG de Airflow) se ejecuta diariamente y activa dos tareas secuenciales:

Tarea 1: Ejecuta el primer job de Dataflow.

Tarea 2: Ejecuta el segundo job de Dataflow después de finalizar la primera.

Los resultados procesados son almacenados en un bucket destino en Cloud Storage.


📦 Componentes del Proyecto
1. Servicio: Dataflow
Archivos:

composer_dataflow.py

composer_dataflow1.py

Función: Cada archivo representa un pipeline de Apache Beam que se ejecuta como job de Dataflow para procesar datos de forma escalable.

Ubicación: Estos archivos deben estar cargados previamente en un bucket GCS accesible por Cloud Composer.


2. Servicio: Cloud Composer (Apache Airflow)
Archivo: dag.py

Función: Define un DAG con dos tareas DataflowCreatePythonJobOperator que ejecutan jobs de Dataflow en orden secuencial.

Frecuencia: El DAG está configurado para ejecutarse una vez al día (schedule_interval=timedelta(days=1)).


3. Servicio: Cloud Storage
Uso:

Staging y temp: Requeridos por los jobs de Dataflow durante su ejecución.

Results: Los archivos de salida generados por los pipelines serán almacenados aquí.

Revisión: Accede al bucket destino (gs://beam_dataflow_cl/results/) para validar la salida de los procesos.


✅ Requisitos Previos
Tener habilitados los siguientes servicios en GCP:

Cloud Composer

Dataflow

Cloud Storage

Asegurarte de que la cuenta de servicio usada por Composer tenga los permisos necesarios:

roles/composer.worker

roles/dataflow.admin

roles/storage.admin


🛠️ Cómo Ejecutar
Subir los archivos composer_dataflow.py y composer_dataflow1.py a tu bucket GCS.

Subir el archivo dag.py a la carpeta dags/ de tu entorno de Composer.

Verifica en el entorno de Airflow que el DAG esté habilitado y programado.

Espera la ejecución automática o dispara el DAG manualmente para probarlo.

Revisa el bucket destino para verificar los resultados.








