import mysql.connector as c

conn = c.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bca_5a",
)

cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE student_details(
        stud_id INT(11) PRIMARY KEY AUTO_INCREMENT,
        stud_name VARCHAR(50),
        stud_city VARCHAR(50), 
    )'''
)

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)