import functions_framework
from googleapiclient.discovery import build
from google.auth import default

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function que lanza un job en Dataflow desde una plantilla."""

    # Obtener credenciales y proyecto actual
    credentials, project_id = default()

    # Crear cliente de Dataflow
    dataflow = build("dataflow", "v1b3", credentials=credentials)
    
    # Parámetros de entrada
    job_name = "dataflow-job-triggered"
    region = "us-central1"
    gcs_template_path = "gs://beam_dataflow_cl/templates/pipeline_template"  # reemplaza TU_BUCKET

    # Ejecutar el job en Dataflow usando la plantilla
    response = dataflow.projects().locations().templates().launch(
        projectId=project_id,
        location=region,
        gcsPath=gcs_template_path,  # <--- va aquí, no en body
        body={
                "jobName": job_name
            }
        ).execute()


    return f"Job lanzado con éxito: {response.get('job', {}).get('id')}", 200
