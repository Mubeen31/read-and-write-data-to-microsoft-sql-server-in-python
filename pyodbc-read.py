import pyodbc as odbc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

sql_conn = odbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=sensorstemphum.database.windows.net;"
                        "Database=weatherdata;"
                        "Trusted_Connection = yes;"
                        "UID=temphum;"
                        "PWD=Temp!hum;"
                        )
sql_query = f"""SELECT
DateTime,
Voltage,
ValueCurrent
FROM dbo.WeatherSensorsData
ORDER BY
DateTime
"""
df = pd.read_sql(sql_query, sql_conn)
print(df)
