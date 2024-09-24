import mysql.connector as c

conn = c.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bca_5a"
)

cursor = conn.cursor()

cursor.execute("ALTER TABLE student_details ADD COLUMN stud_mobile VARCHAR(10)")