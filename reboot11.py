print("숫자 입력")
nums = list(map(int, input().split()))

for i in nums:
    cnt = 0
    if i == 1:
        continue
    # 1은 소수가 아니니까
    # 1인 경우 다시 반복문 시작으로 돌아가라
    # 소수를 구해 소수를 출력하는 거니까 1은 출력 못하게 한 것
    for j in range(2, i+1):
        # 2~자기 자신 + 1 => 범위 2~자기 자신
        if i % j == 0:
            # 리스트 값 % 2~자기 자신 == 0이 되면
            cnt += 1
            # cnt 변수에 +1
    if cnt == 1:
        print(i)
