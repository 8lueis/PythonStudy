# 남이 만든 코드를 내가 쓸 수 있도록 불러오는 기능
import math

# pi 값 출력
print(math.pi)

# 원의 반지름 제시
radius = 5.0
# 반지름 거듭 제곱 X 파이
area = (radius ** 2) * math.pi

print("area: " + str(area))

# print("area : "+area)
# str 값이 먼저 오면 그 뒤 값도 일반적으로 str이 와야 '+' 연산이 되는데
# float -> str downcasting이라서 오류가 나는 듯 (컴파일러가 안 해 줌)

# 다른 방법 ',' 사용하기
print("area ==> ", area)