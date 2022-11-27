import pandas as pd
from sqlalchemy import create_engine

server_name = 'sensorstemphum.database.windows.net'
database_name = 'weatherdata'
user_name = 'temphum'
password = 'Temp!hum'

eng = create_engine('mssql+pyodbc://'+user_name+':'+password+'@'+server_name+'/weatherdata?driver=SQL+Server')

df = pd.read_sql_table('Customer', eng, columns = ['CustomerID',
                                                   'CustomerName',
                                                   'Phone'])
print(df)
