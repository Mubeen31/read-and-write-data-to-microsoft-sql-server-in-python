import pyodbc as odbc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

sql_conn = odbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=;"
                        "Database=;"
                        "Trusted_Connection = yes;"
                        "UID=;"
                        "PWD=;"
                        )
sql_query = f"""SELECT
DateTime,
Voltage,
ValueCurrent
FROM type table name here
ORDER BY
DateTime
"""
df = pd.read_sql(sql_query, sql_conn)
print(df)
