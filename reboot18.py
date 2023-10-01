# 자연수 N이 주어지면 N의 각 자릿수의 합을 구하기
# 123 -> 1+2+3 = 6
def solution(n):
    answer = 0
    while n > 0:
        # 나머지
        answer += (n % 10)
        # 몫
        n //= 10
    return answer

print("숫자 입력: ")
num = int(input())
result = solution(num)
print(result)