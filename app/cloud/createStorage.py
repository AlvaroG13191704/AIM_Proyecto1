import sys
from google.oauth2 import service_account
from google.cloud import storage

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")

def create_cloud(file_data, destination_blob_name):
  """Uploads file data to the bucket."""
  storage_client = storage.Client(credentials=google_credentials)
  bucket = storage_client.bucket("iam_project1_bucket")
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_string(file_data)

  print(f"File data uploaded to {destination_blob_name}.")


if __name__ == "__main__":
  file_data = '''This is the content of the text file.
  It can have multiple lines and contain any text data.
  '''

  create_cloud(
      file_data=file_data,
      destination_blob_name="ARCHIVOS/carpeta1/example3.txt",
  )
#  create_cloud(bucket_name="iam_project1_bucket", file_data=body, destination_blob_name=f"ARCHIVOS{path[:-1]}{name}")

