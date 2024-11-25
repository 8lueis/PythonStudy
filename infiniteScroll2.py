import pymysql.cursors
from pymysql import MySQLError

# fetchall로 fetchmany와 같은 역할 수행하도록 작성해 보기 
# how? limit, offset 사용 

connection = pymysql.connect(
        host='',
        port=3309,  
        user='',
        password='',
        database='testdb',
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor
    )

cursor = connection.cursor()



x = 0

while True:
    sql = "SELECT id, NAME, qty From inventory ORDER BY id LIMIT 15 OFFSET %s"
    cursor.execute(sql, (x,))

    result = cursor.fetchall()

    if(len(result)==0):
        break

    for record in result:
        print(record)
    
    print("데이터 출력 완료\n")

    x += 15 

