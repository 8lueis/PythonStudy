# n이 어떤 양의 정수 x의 제곱이면 x 값 출력
# n이 x의 제곱이 아니면 -1

def solution(n):
    # 초기화 -> 값 자체는 큰 상관 Xx
    # 하지만 제곱근이 아니면 -1을 return 해야 함
    # 그 외 제곱근ㅇ ㅣ맞을 때 말곤 갱신이 Xx
    answer = -1
    # n의 제곱근 구하는 방식
    rst = n ** 0.5

    if rst == int(rst):
        # 제곱근의 몫(정수 값)이 rst와 같으면
        answer = rst # answer의 갱신

    return answer

print("숫자 입력")
num = int(input())
result = solution(num)
print(result)