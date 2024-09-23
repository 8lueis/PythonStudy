# 자연수 n을 뒤집어서 배열 형태로 리턴
# ex. n: 12345 -> return [5,4,3,2,1]
def s4(n):
    ls = list(str(n))
    # list로 n 값 변환
    # str으로 변환하는 이유: str(n)을 사용하면 각 자리 숫자에 접근하기 쉽기 때문
    # 즉 뒤집은 숫자를 배열 형태로 출력하고자 한 것
    # 안 하면 TypeError: 'int' object is not iterable
    ls.sort(reverse=True)
    # 리스트를 내림차순으로 정렬함
    return ls

print("숫자 입력:")
num = int(input())
result = s4(num)
print(result)