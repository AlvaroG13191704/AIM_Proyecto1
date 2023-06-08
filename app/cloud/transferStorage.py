from google.oauth2 import service_account
from google.cloud import storage
from google.api_core.exceptions import NotFound

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


def transfer_cloud(blob_name, destination_blob_name):
    """Moves a blob from one bucket to another with a new name, and deletes the source blob."""
    storage_client = storage.Client(credentials=google_credentials)

    source_bucket = storage_client.bucket("iam_project1_bucket")
    destination_bucket = storage_client.bucket("iam_project1_bucket")

    try:
        if blob_name.endswith("/"):
            # CHECK IF THE ORIGIN DIRECTORY EXISTS
            blobs = list(source_bucket.list_blobs(prefix=blob_name))
            if not blobs:
                print(f"Directory {blob_name} does not exist or does not contain any files.")
                return False
            # CHECK IF THE DESTINATION DIRECTORY EXISTS
            blobs_destination = list(destination_bucket.list_blobs(prefix=destination_blob_name))
            if not blobs_destination:
                print(f"Directory {destination_blob_name} does not exist.")
                return False
            # Check if the blobs of the destination already exist - add (1) to the name or 
            list_names_exist = []
            for blob in blobs_destination:
                if blob.name[len(destination_blob_name):] in [blob.name[len(blob_name):] for blob in blobs]:
                    # append the name to the list
                    list_names_exist.append(blob.name[len(destination_blob_name):])
                    # print(f"File {blob.name[len(destination_blob_name):]} already exists in {destination_blob_name}")

            for blob in blobs:
                if blob.name[len(blob_name):] in list_names_exist:
                    # change the name add (1)
                    destination = destination_blob_name + str(blob.name[len(blob_name):].replace(".txt", "(1).txt"))
                    source_blob = source_bucket.blob(blob.name)
                    destination_blob = destination_bucket.blob(destination)
                    destination_blob.rewrite(source_blob)   
                    # Delete the source blob
                    source_blob.delete()

                # Move the blob to the destination
                destination = destination_blob_name + str(blob.name[len(blob_name):])
                source_blob = source_bucket.blob(blob.name)
                destination_blob = destination_bucket.blob(destination)
                destination_blob.rewrite(source_blob)

                # Delete the source blob
                source_blob.delete()

            print("Files moved successfully.")
        else:
            # CHECK IF THE DESTINATION DIRECTORY EXISTS
            blobs = list(destination_bucket.list_blobs(prefix=destination_blob_name))
            if not blobs:
                print(f"Directory {destination_blob_name} does not exist.")
                return False
            # Check if the blobs of the destination already exist
            for blob in blobs:
                if blob.name[len(destination_blob_name):] == blob_name.split("/")[::-1][0]:
                    # change the name add (1)
                    destination = destination_blob_name + str(blob_name.split("/")[::-1][0].replace(".txt", "(1).txt"))
                    source_blob = source_bucket.blob(blob_name)
                    destination_blob = destination_bucket.blob(destination)
                    destination_blob.rewrite(source_blob)
                    # Delete the source blob
                    source_blob.delete()

            destination = destination_blob_name + str(blob_name.split("/")[::-1][0])
            source_blob = source_bucket.blob(blob_name)
            destination_blob = destination_bucket.blob(destination)
            destination_blob.rewrite(source_blob)

            # Delete the source blob
            source_blob.delete()

            print(
                "Blob {} moved to blob {} ".format(
                    source_blob.name,
                    destination_blob.name,
                )
            )
    except NotFound:
        print(f"Blob or directory {blob_name} does not exist. Error: {NotFound}")
        return False

    return None


if __name__ == "__main__":
    transfer_cloud(
      blob_name="ARCHIVOS/carpeta5/",
      destination_blob_name="ARCHIVOS/carpeta 2/",
    )