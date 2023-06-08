import sys
from google.oauth2 import service_account
from google.cloud import storage

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


def delete_cloud(blob_name):
  """Deletes a blob or directory from the bucket."""
  storage_client = storage.Client(credentials=google_credentials)
  bucket = storage_client.bucket("iam_project1_bucket")
  blob = bucket.blob(blob_name)

  if blob_name.endswith("/"):
      # Directory deletion
      blobs = list(bucket.list_blobs(prefix=blob_name))  # Convert the iterator to a list

      if not blobs:
          print(f"Directory {blob_name} does not exist.")
          return False

      for blob in blobs:
          blob.delete()
      print(f"Directory {blob_name} deleted.")
  else:
      # Single blob deletion
      if not blob.exists():
          print(f"Blob {blob_name} does not exist.")
          return False

      blob.delete()
      print(f"Blob {blob_name} deleted.")

  return True


if __name__ == "__main__":
  delete_cloud(blob_name="ARCHIVOS/carpeta3/") # delete the directory
  delete_cloud(blob_name="ARCHIVOS/carpeta 2/prueba 2.txt") # delete the file
