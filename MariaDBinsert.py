import pymysql.cursors
from pymysql import MySQLError

# 1. MariaDB 데이터베이스에 연결 설정
try:
    connection = pymysql.connect(
        host='localhost',
        port='',  
        user='',
        password='',  
        database='',
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor
    )

except MySQLError as e:
    print(f"데이터베이스 연결 오류: {e}")
    exit(1)  # 연결 실패 시 스크립트를 종료

try:
    with connection:
        with connection.cursor() as cursor:
             # 2. SQL 쿼리 정의
             sql = "INSERT INTO `student` (`studentID`, `name`) VALUES (%s, %s)"
             # 3. 삽입할 데이터 리스트 정의
             students = [
                 ('210', 'kyung'),
                 ('211', 'suck'),
                 ('212', 'jae'),
                 ('213', 'min')
             ]
           
            # 4. 여러 개의 레코드를 한 번에 삽입
             cursor.executemany(sql, students)
            
             result = cursor.fetchall()
             for record in result:
                 print(record)
            # 5. 트랜잭션 커밋
        connection.commit()
except MySQLError as e:
    print(f"SQL 명령 실행 중 오류 발생: {e}")
    # 필요에 따라 롤백을 수행
    connection.rollback()
finally:
    # 5. 연결이 닫혔는지 확인
    if connection.open:
        connection.close()
        print("데이터베이스 연결이 종료되었습니다.")
