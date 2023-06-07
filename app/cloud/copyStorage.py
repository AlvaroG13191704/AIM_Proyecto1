from google.oauth2 import service_account
from google.cloud import storage

google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


def copy_cloud(blob_name, destination_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    storage_client = storage.Client(credentials=google_credentials)

    source_bucket = storage_client.bucket("iam_project1_bucket")
    destination_bucket = storage_client.bucket("iam_project1_bucket")

    if blob_name.endswith("/"):
        blobs = list(source_bucket.list_blobs(prefix=blob_name))
        if not blobs:
            print(f"Directory {blob_name} does not contain any files.")
            return False

        for blob in blobs:
            destination = destination_blob_name + str(blob.name[len(blob_name):])
            source_blob = source_bucket.blob(blob.name)
            destination_blob = destination_bucket.blob(destination)
            destination_blob.rewrite(source_blob)

        print("Files copied successfully.")
    else:
        source_blob = source_bucket.blob(blob_name)
        destination_blob = destination_bucket.blob(destination_blob_name)
        destination_blob.rewrite(source_blob)

        print(
            "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
                source_blob.name,
                source_bucket.name,
                destination_blob.name,
                destination_bucket.name,
            )
        )

    return None


if __name__ == "__main__":
    copy_cloud(
        blob_name="ARCHIVOS/carpeta1/",
        destination_blob_name="ARCHIVOS/carpeta 2/",
    )




# from google.oauth2 import service_account
# from google.cloud import storage

# google_credentials = service_account.Credentials.from_service_account_file("app/cloud/key.json")


# def copy_cloud(blob_name, destination_blob_name):
#   """Copies a blob from one bucket to another with a new name."""
#   storage_client = storage.Client(credentials=google_credentials)

#   source_bucket = storage_client.bucket("iam_project1_bucket")
#   source_blob = source_bucket.blob(blob_name)
#   destination_bucket = storage_client.bucket("iam_project1_bucket")

#   destination_generation_match_precondition = 0

#   # print(source_blob)
#   if blob_name.endswith("/"):
#     # print list of blobs of the directory
#     blobs = list(source_bucket.list_blobs(prefix=blob_name))  # Convert the iterator to a list
#     # check if the directory exists
#     if not blobs:
#       print(f"Directory {blob_name} does not exist.")
#       return False
#     # print the list of blobs
#     for blob in blobs:
#       # save the name of the blob
#       pathFile = blob.name.split("/")[::-1][0] # get the last element of the list
#       destination = destination_blob_name+pathFile
#       #  copy the blob to the new directory
#       blob_copy = source_bucket.copy_blob(
#         blob, destination_bucket, destination, if_generation_match=destination_generation_match_precondition,
#       )
#     # print the blob
#     print("Files copied successfully.")
#   else:
#     # Single blob deletion
#     if not source_blob.exists():
#       print(f"Blob {blob_name} does not exist.")
#       return False
#     # print the blob
#     print(source_blob)
#   return None


#   blob_copy = source_bucket.copy_blob(
#       source_blob, destination_bucket, destination_blob_name, if_generation_match=destination_generation_match_precondition,
#   )

#   print(
#       "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
#           source_blob.name,
#           source_bucket.name,
#           blob_copy.name,
#           destination_bucket.name,
#       )
#   )


# if __name__ == "__main__":
#   copy_cloud(
#     # blob_name="ARCHIVOS/carpeta1/example.txt",
#     blob_name="ARCHIVOS/carpeta1/",
#     destination_blob_name="ARCHIVOS/carpeta 2/",
#   )

# Configure -type->local -encrypt_log->false -encrypt_read->false
# create -name->prueba1.txt -path->/carpeta1/ -body->"Este es el contenido del archivo 1"
# create -namE->"prueba 2.txt" -path->/"carpeta 2"/ -boDy->"Este es el contenido del archivo 2"
# delete -path->/carpeta1/ -name->prueba1.txt
# bakcup
