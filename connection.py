import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='androidbackend',
    port=3306
)
