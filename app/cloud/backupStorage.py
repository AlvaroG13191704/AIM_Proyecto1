# if the configuration is cloud, download the backup file from the cloud storage and add it to the local storage
from google.oauth2 import service_account
from google.cloud import storage
import os
import json

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")

def backup_cloud(bucket_name, backup_file):
    """Backs up all files and directories from a bucket to a JSON file."""
    storage_client = storage.Client(credentials=google_credentials)
    bucket = storage_client.get_bucket(bucket_name)

    blob_list = list(bucket.list_blobs())

    backup_data = {}
    
    for blob in blob_list:
        if blob.name.endswith("/"):  # Directory
            directory_name = blob.name.rstrip("/")
            backup_data[directory_name] = []
            
            # Get files within the directory
            sub_blob_list = list(bucket.list_blobs(prefix=blob.name))
            for sub_blob in sub_blob_list:
                if not sub_blob.name.endswith("/"):  # Exclude sub-directories
                    file_name = sub_blob.name.split("/")[-1]
                    file_contents = sub_blob.download_as_text()
                    backup_data[directory_name].append({"file_name": file_name, "file_contents": file_contents})
        else:  # File in the root of the bucket
            file_name = blob.name.split("/")[-1]
            file_contents = blob.download_as_text()
            backup_data[file_name] = file_contents

    with open(backup_file, "w") as file:
        json.dump(backup_data, file, indent=4)

    print(f"Backup completed. Backup data saved to {backup_file}")


def restore_backup(backup_file):
    """Restores the backup data and recreates the directories locally."""
    with open(backup_file, "r") as file:
        backup_data = json.load(file)

    for name, content in backup_data.items():
        if isinstance(content, list):  # Directory
            directory_path = f"backup/{name}"  # Change the path as per your requirement
            os.makedirs(directory_path, exist_ok=True)

            for file_data in content:
                file_name = file_data["file_name"]
                file_contents = file_data["file_contents"]
                with open(f"{directory_path}/{file_name}", "w") as file:
                    file.write(file_contents)
        else:  # File
            with open(f"backup/{name}", "w") as file:  # Change the path as per your requirement
                file.write(content)

    print("Backup restored successfully.")


if __name__ == "__main__":
    bucket_name = "iam_project1_bucket"
    backup_file = "bucket_backup.json"

    # Backup the bucket
    backup_cloud(bucket_name, backup_file)

    # Restore the backup
    restore_backup(backup_file)
