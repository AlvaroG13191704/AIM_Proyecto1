from google.oauth2 import service_account
from google.cloud import storage
from google.api_core.exceptions import NotFound

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


def copy_cloud(blob_name, destination_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    storage_client = storage.Client(credentials=google_credentials)

    source_bucket = storage_client.bucket("iam_project1_bucket")
    destination_bucket = storage_client.bucket("iam_project1_bucket")

    path_name = "ARCHIVOS" + blob_name 
    path_destination = "ARCHIVOS" + destination_blob_name
    try:
        if path_name.endswith("/"):
            # CHECK IF THE ORIGIN DIRECTORY EXISTS
            blobs = list(source_bucket.list_blobs(prefix=path_name))
            if not blobs:
                print(f"Directory {path_name} does not exist or does not contain any files.")
                return False
            # CHECK IF THE DESTINATION DIRECTORY EXISTS
            blobs_destination = list(destination_bucket.list_blobs(prefix=path_destination))
            if not blobs_destination:
                print(f"Directory {path_destination} does not exist.")
                return False
            # Check if the blobs of the destination already exist
            for blob in blobs_destination:
                if blob.name[len(path_destination):] in [blob.name[len(path_name):] for blob in blobs]:
                    print(f"File {blob.name[len(path_destination):]} already exists in {path_destination}")
                    return False

            for blob in blobs:
                # Copy the blob to the destination
                destination = path_destination + str(blob.name[len(path_name):])
                source_blob = source_bucket.blob(blob.name)
                destination_blob = destination_bucket.blob(destination)
                destination_blob.rewrite(source_blob)

            print("Files copied successfully.")
        else:
            # CHECK IF THE DESTINATION DIRECTORY EXISTS
            blobs = list(destination_bucket.list_blobs(prefix=path_destination))
            if not blobs:
                print(f"Directory {path_destination} does not exist.")
                return False
            # Check if the blobs of the destination already exist
            for blob in blobs:
                if blob.name[len(path_destination):] == blob_name.split("/")[::-1][0]:
                    print(f"File {blob_name.split('/')[::-1][0]} already exists in {path_destination}")
                    return False

            destination = path_destination + str(path_name.split("/")[::-1][0])
            source_blob = source_bucket.blob(path_name)
            destination_blob = destination_bucket.blob(destination)
            destination_blob.rewrite(source_blob)
            print(
                "Blob {} copied to blob {} ".format(
                    source_blob.name,
                    destination_blob.name,
                )
            )
    except NotFound:
        print(f"Blob or directory {path_name} does not exist.")

    return None


if __name__ == "__main__":
    copy_cloud(
        blob_name="/carpeta1/",
        destination_blob_name="/carpeta 2/",
    )


# from google.oauth2 import service_account
# from google.cloud import storage
# from google.api_core.exceptions import NotFound

# google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


# def copy_cloud(blob_name, destination_blob_name):
#   """Copies a blob from one bucket to another with a new name."""
#   storage_client = storage.Client(credentials=google_credentials)

#   source_bucket = storage_client.bucket("iam_project1_bucket")
#   destination_bucket = storage_client.bucket("iam_project1_bucket")

#   try:
#     if blob_name.endswith("/"):
#         # CHECK IF THE ORIGIN DIRECTORY EXISTS
#         blobs = list(source_bucket.list_blobs(prefix=blob_name))
#         if not blobs:
#             print(f"Directory {blob_name} does not exist or does not contain any files.")
#             return False
#         # CHECK IF THE DESTINATION DIRECTORY EXISTS
#         blobs_destination = list(destination_bucket.list_blobs(prefix=destination_blob_name))
#         if not blobs_destination:
#             print(f"Directory {destination_blob_name} does not exist.")
#             return False
#         # Check if the blobs of the destination already exist
#         for blob in blobs_destination:
#             if blob.name[len(destination_blob_name):] in [blob.name[len(blob_name):] for blob in blobs]:
#                 print(f"File {blob.name[len(destination_blob_name):]} already exists in {destination_blob_name}")
#                 return False

#         for blob in blobs:
#             # WHile or loop to check directories nested
#             destination = destination_blob_name + str(blob.name[len(blob_name):])
#             source_blob = source_bucket.blob(blob.name)
#             destination_blob = destination_bucket.blob(destination)
#             destination_blob.rewrite(source_blob)

#         print("Files copied successfully.")
#     else:
#         # CHECK IF THE DESTINATION DIRECTORY EXISTS
#         blobs = list(destination_bucket.list_blobs(prefix=destination_blob_name))
#         if not blobs:
#             print(f"Directory {destination_blob_name} does not exist.")
#             return False
#         # Check if the blobs of the destination already exist
#         for blob in blobs:
#             if blob.name[len(destination_blob_name):] == blob_name.split("/")[::-1][0]:
#                 print(f"File {blob_name.split('/')[::-1][0]} already exists in {destination_blob_name}")
#                 return False
            
#         destination = destination_blob_name + str(blob_name.split("/")[::-1][0])
#         source_blob = source_bucket.blob(blob_name)
#         destination_blob = destination_bucket.blob(destination)
#         destination_blob.rewrite(source_blob)
#         print(
#             "Blob {} copied to blob {} ".format(
#                 source_blob.name,
#                 destination_blob.name,
#             )
#         )
#   except NotFound:
#       print(f"Blob or directory {blob_name} does not exist.")

#   return None


# if __name__ == "__main__":
#   copy_cloud(
#     blob_name="ARCHIVOS/carpeta 2/",
#     destination_blob_name="ARCHIVOS/carpeta1/",
#   )

# Configure -type->local -encrypt_log->false -encrypt_read->false
# create -name->prueba1.txt -path->/carpeta1/ -body->"Este es el contenido del archivo 1"
# create -namE->"prueba 2.txt" -path->/"carpeta 2"/ -boDy->"Este es el contenido del archivo 2"
# delete -path->/carpeta1/ -name->prueba1.txt
# bakcup
