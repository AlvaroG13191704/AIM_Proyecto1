from google.oauth2 import service_account
from google.cloud import storage

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")

def create_cloud(name, file_data, destination_blob_name):
  """Uploads file data to the bucket."""
  storage_client = storage.Client(credentials=google_credentials)
  bucket = storage_client.bucket("iam_project1_bucket")
  blob = bucket.blob(destination_blob_name + name)

  # CHECK IF THE FILE ALREADY EXISTS
  if blob.exists():
    print(f"File {destination_blob_name + name} already exists.")
    return False

  blob.upload_from_string(file_data)

  print(f"File data uploaded to {destination_blob_name + name}.")

