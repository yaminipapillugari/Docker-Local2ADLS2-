
from azure.storage.filedatalake import DataLakeServiceClient

#Config parser parses the config files
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

storage_account_name = config['cred']['san']
storage_account_key = config['cred']['sak']
print(storage_account_name)
print(storage_account_key)

#Establishing a connection to adls2
def initialize_storage_account(storage_account_name, storage_account_key):
    try:
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
        print("ADLS connection established successfully")

    except Exception as e:
        print(e)


initialize_storage_account(storage_account_name, storage_account_key)

#Upload a file to a directory
def upload_file_to_directory(data_frame,filename):
    try:
        file_system_client = service_client.get_file_system_client(file_system="my-file-system")

        directory_client = file_system_client.get_directory_client("Docker_file")
        file_client = directory_client.create_file(filename)
        print(data_frame)
        df_byte = data_frame.to_json().encode()
        print(df_byte)
        file_client.upload_data(df_byte, overwrite=True)
        # file_client.append_data(data=encrypted_data, offset=0, length=len(encrypted_data))

        # file_client.flush_data(len(file_contents))
        # logger.info("Uploaded "+filename)

    except Exception as e:
        print(e)