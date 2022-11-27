import pyodbc as odbc

sql_conn = odbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=sensorstemphum.database.windows.net;"
                        "Database=weatherdata;"
                        "Trusted_Connection = yes;"
                        "UID=temphum;"
                        "PWD=Temp!hum;"
                        )
cursor = sql_conn.cursor()
date_time = '2022-10-09 19:25:24'
voltage = 0.14648
value_current = 0.0
count = cursor.execute("""
                       INSERT INTO 
                       dbo.WeatherSensorsData (DateTime,
                       Voltage,
                       ValueCurrent)
                       VALUES (?,?,?)""",
                       date_time, voltage, value_current).rowcount
sql_conn.commit()
print('Rows inserted: ' + str(count))

