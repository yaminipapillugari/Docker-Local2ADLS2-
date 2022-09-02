import pyodbc

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

server = config['sqlcred']['server']
database = config['sqlcred']['database']
username = config['sqlcred']['username']
password = config['sqlcred']['password']
driver = config['sqlcred']['driver']
print(database)
print(username)

def sqlconnection(df):
    conn=pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    print("SQL connection established successfully")
    # Create table in DB
    cursor.execute("drop table if exists products_docker1")
    cursor.execute('''
		CREATE TABLE products_docker1 (
			ProductID int,
			ProductName nvarchar(50),
			Rate int
			)
               ''')
    print("created a table in azure sql")
    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
        cursor.execute('''
                    INSERT INTO products_docker1 (ProductID, ProductName, Rate)
                    VALUES (?,?,?)
                    ''',
                       row.ProductID,
                       row.ProductName,
                       row.Rate
                       )
        # row = cursor.fetchone()
        # for row in list(row):
        #     print(str(row[0]))
    conn.commit()