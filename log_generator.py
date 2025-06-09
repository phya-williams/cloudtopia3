import time, uuid, json
from azure.storage.blob import BlobServiceClient

connect_str = "<your_connection_string>"  # From Access Keys
container_name = "weatherdata"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

while True:
    log = {
        "id": str(uuid.uuid4()),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "weather": "rainy",
        "temperature": 75 + (uuid.uuid4().int % 10)
    }
    log_data = json.dumps(log)
    blob_name = f"log_{log['timestamp'].replace(' ', '_').replace(':', '-')}.json"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(log_data, overwrite=True)
    print(f"Uploaded: {blob_name}")
    time.sleep(4)
