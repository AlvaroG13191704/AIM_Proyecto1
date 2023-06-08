from google.oauth2 import service_account
from google.cloud import storage
from google.api_core.exceptions import NotFound

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


def modify_cloud(blob_name, new_content):
    """Modifies the content of a file in Google Cloud Storage."""
    storage_client = storage.Client(credentials=google_credentials)

    bucket = storage_client.bucket("iam_project1_bucket")

    try:
        blob = bucket.blob(blob_name)
        if blob.exists():
            blob.upload_from_string(new_content)
            print(f"Content of file {blob_name} modified successfully.")
        else:
            print(f"File {blob_name} does not exist.")
            return False
    except NotFound:
        print(f"File or Directory {blob_name} does not exist.")

    return None


if __name__ == "__main__":
    modify_cloud(
        blob_name="ARCHIVOS/carpeta3/example.txt",
        new_content="This is the modified content of the file.",
    )
