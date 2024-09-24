import mysql.connector as c

conn = c.connect(
    host = "localhost",
    user = "root",
    password = ""
)

print(conn)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE bca_5a")
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)