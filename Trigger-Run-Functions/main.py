import functions_framework
from google.cloud import storage

# Define the destination bucket for valid files
VALID_FILES_BUCKET = "output_trigger"

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]

    # Initialize GCS client
    storage_client = storage.Client()
    source_bucket = storage_client.bucket(bucket)
    blob = source_bucket.blob(name)

    # Reload blob metadata to ensure size is fetched
    blob.reload()

    # Get file size in bytes
    file_size = blob.size

    # Ensure file size is not None
    if file_size is None:
        print(f"Unable to determine the size for {name}. Skipping.")
        return

    max_size = 2 * 1024 * 1024  # 2MB in bytes

    if file_size < max_size:
        # Move the file to the "large_files/" folder in the destination bucket
        destination_bucket = storage_client.bucket(VALID_FILES_BUCKET)
        new_blob_name = f"large_files/{name}"  # Add folder prefix
        new_blob = source_bucket.copy_blob(blob, destination_bucket, new_blob_name)

        # Delete the original file
        blob.delete()

        print(f"File {name} moved to {VALID_FILES_BUCKET}/large_files/{name} because < 2MB.")
    else:
        print(f"The file {name} is larger than (> 2MB). No action has been taken.")

