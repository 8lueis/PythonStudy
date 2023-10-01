# 팩토리얼 구하기
# 어떤 양의 정수 n이 있으면 1부터 n까지의 모든 양의 정수를 곱한 값을 구함 == 시작 값 주의

print("숫자 입력")
n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        # n이 정수면 1부터 n+1(n의)값을
        result *= i
        # result = result * i (1~10) 값의 곱셈이 반복

print(result)