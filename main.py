import os
import sqlconn
# assign directory
from adlsconn import upload_file_to_directory
file_path = os.environ.get('filepath')
# file_path = r'C:\Project_sample'
import pandas as pd
print(file_path)

for file in os.listdir(file_path):
    print(file)
    df = pd.read_csv(os.path.join(file_path, file))
    upload_file_to_directory(df, file)
    sqlconn.sqlconnection(df)