from google.cloud import storage
import argparse

def simple_file_reader(bucket_name, file_path):
    """Función independiente para leer archivos de GCS"""
    bucket_name = "beam_dataflow_cl"  # Solo nombre del bucket
    file_path = "origin/data.csv"     # Ruta relativa del archivo
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_path)
    
    content = blob.download_as_text()
    print("Contenido del archivo:")
    print("=" * 50)
    print(content)
    print("=" * 50)

if __name__ == "__main__":
    # Configurar argumentos de línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', type=str, default="beam_dataflow_cl", help="Nombre del bucket")
    parser.add_argument('--file', type=str, default="origin/data.csv", help="Ruta del archivo")
    args = parser.parse_args()
    
    simple_file_reader(args.bucket, args.file)
    
    #simple_file_reader()
    
