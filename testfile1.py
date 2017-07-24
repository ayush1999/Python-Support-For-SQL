import sqlite3 as sl
connection = sl.connect('company.db')
cursor = connection.cursor()

sql_command="""
CREATE TABLE TABLE1(
NAME       VARCHAR(20),
ID         INT,
AMOUNT     INT
);"""

cursor.execute(sql_command)
connection.commit()
connection.close()
