import pandas as pd
from sqlalchemy import create_engine

server_name = ''
database_name = ''
user_name = ''
password = ''

eng = create_engine('mssql+pyodbc://'+user_name+':'+password+'@'+server_name+'/type database name here?driver=SQL+Server')

df = pd.read_sql_table('Customer', eng, columns = ['CustomerID',
                                                   'CustomerName',
                                                   'Phone'])
print(df)
