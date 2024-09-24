import mysql.connector as c

conn = c.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bca_5a"
)

cursor = conn.cursor()

qry = '''INSERT INTO student_details (stud_name, stud_city, stud_mobile) VALUES (%s, %s, %s)'''

val = ('Uday2', 'Shapur', '7016489410')

cursor.execute(qry, val)

conn.commit()