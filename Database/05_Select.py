import mysql.connector as c

conn = c.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "python"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

res = cursor.fetchone()
print(res)
for x in res:
    print(x)