import pymysql.cursors
from pymysql import MySQLError

# 1. MariaDB 데이터베이스에 연결 설정
try:
    connection = pymysql.connect(
        host='localhost',
        port='',  # 올바른 포트인지 확인하세요
        user='',
        password='',  # 강력한 비밀번호 사용을 권장합니다
        database='',
        charset='utf8mb4',  # utf8mb4가 일반적으로 utf8보다 더 선호됩니다
        cursorclass=pymysql.cursors.DictCursor
    )
except MySQLError as e:
    print(f"데이터베이스 연결 오류: {e}")
    exit(1)  # 연결 실패 시 스크립트를 종료합니다

except MySQLError as e:
    print(f"데이터베이스 연결 오류: {e}")
    exit(1)  # 연결 실패 시 스크립트를 종료

try:
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `studentID`, `name` FROM `student` WHERE `name` LIKE %s"
            pattern = '%n%'
            cursor.execute(sql, (pattern,))
            results = cursor.fetchall()
           
            print(f"조회된 레코드 수: {len(results)}")
            if results:
                for row in results:
                    print(f"학생 ID: {row['studentID']}, 이름: {row['name']}")
            else:
                print("조건에 맞는 데이터가 없습니다.")
           
             # 5. 트랜잭션 커밋
        connection.commit()
except MySQLError as e:
    print(f"SQL 명령 실행 중 오류 발생: {e}")
    # 필요에 따라 롤백을 수행할 수 있습니다
    connection.rollback()
finally:
    # 5. 연결이 닫혔는지 확인
    if connection.open:
        connection.close()
        print("데이터베이스 연결이 종료되었습니다.")
