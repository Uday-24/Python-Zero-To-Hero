import mysql.connector as c

con = c.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "python",
)

cursor = con.cursor()

# cursor.execute('CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), city VARCHAR(255))')

# cursor.execute("SHOW TABLES")

# qry = "INSERT INTO student (name, city) VALUES (%s, %s)"
# val = ("Uday", "Shapur")
# cursor.execute(qry, val)


qry = "INSERT INTO student (name, city) VALUES (%s, %s)"
val = [
    ('Disha', 'Timbavadi'),
    ('Vishv', 'Near Patel Samal'),
    ('Mihir', 'Manglore'),
    ('Darshit', 'Junagadh')
]
cursor.executemany(qry, val)
con.commit()