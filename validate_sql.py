import mysql.connector as  con
from mysql.connector import errorcode as errcode


config = {
        'user': 'retail_user',
        'password': 'itversity',
        'host': '192.168.1.8',
        'database': 'retail'
    }
connection=con.connect(**config)
orders_cursor = connection.cursor()
query = """SELECT * FROM orders LIMIT 10"""
orders_cursor.execute(query)

for order in orders_cursor:
    print(order)

