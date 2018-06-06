from connection import connection

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INT auto_increment PRIMARY KEY, username varchar(255), password varchar(255))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name varchar(255), price double)"
cursor.execute(create_table)

connection.commit()
connection.close()
