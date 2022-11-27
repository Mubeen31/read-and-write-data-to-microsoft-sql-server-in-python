import pandas as pd
from sqlalchemy import create_engine

server_name = ''
database_name = ''
user_name = ''
password = ''

df = pd.read_csv('customer.csv')
df.drop('Unnamed: 0', inplace = True, axis = 1)

eng = create_engine('mssql+pyodbc://'+user_name+':'+password+'@'+server_name+'/type database name here?driver=SQL+Server')
# No need to design table in Microsoft SQL server management studio.
# sqlalchemy will create and design self table.
df.to_sql('Customer', eng, if_exists = 'append', index = False)
