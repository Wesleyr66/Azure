from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

if not connection_string:
    raise ValueError("A string de conexão está vazia. Verifique o arquivo .env.")

def upload_file_blob_client(container_name: str):
    try:
        blob_client = BlobClient.from_connection_string(connection_string, container_name, "arquivo.txt")
        with open("arquivo.txt", "rb") as data:
            blob_client.upload_blob(data)
            print("Arquivo enviado com sucesso")
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo: {e}")

def admin_containers(operation: str):
    try:
        container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name="container2")
        match operation:
            case "list":
                print("Blobs no container:")
                for blob in container_client.list_blobs():
                    print(blob.name)
            case "create":
                container_client.create_container()
                print("Container criado com sucesso")
            case "delete":
                container_client.delete_container()
                print("Container deletado com sucesso")
    except Exception as e:
        print(f"Erro na operação '{operation}': {e}")

def service_blob(container_name: str):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        properties = container_client.get_container_properties()
        print(f"Propriedades do container: {properties}")
        container_client.set_container_access_policy(public_access=PublicAccess.Container)
        print(f"O nível de acesso do container foi alterado para {PublicAccess.Container}")
    except Exception as e:
        print(f"Erro ao acessar o container: {e}")

admin_containers("create")