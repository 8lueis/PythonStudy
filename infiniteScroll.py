import pymysql.cursors
from pymysql import MySQLError

# fetchmany 

connection = pymysql.connect(
        host='',
        port=3309,  
        user='',
        password='',
        database='',
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor
    )

cursor = connection.cursor()

sql = "SELECT id, NAME, qty From inventory ORDER BY id"

cursor.execute(sql)

n = 15

while True:
    result = cursor.fetchmany(n)

    if(len(result)==0):
        break

    for record in result:
        print(record)
    
    print("데이터", n, "개 출력")
    input()

'''
15개씩 출력됨 
'''