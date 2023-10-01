print("시작 숫자 입력:")
start_num = int(input())

print("마지막 숫자 입력:")
last_num = int(input())

total_num = 0

for num in range(start_num, last_num+1):
    error = 0
    if num > 1:
        # 입력 받은 숫자가 1보다 큰 경우
        for i in range(2, num+1):
            # i -> 소수인지 판별하기 위한 값
            # i로 나눠봄
            if num % i == 0:
                error += 1
                # 나눴을 때 나머지가 없이 0인 값이 1 + n번이면
                # error는 1 + n번이 될 것 == 소수가 아님
        if error == 1:
            # error가 1이다 == 소수다
            print(num)
            total_num += 1
            break
            # 범위 중 첫 번째 값이 첫 순서로 비교 되고 있는데
            # 그 값이 소수면 print도 되고 출력이 되고 있음
            # 그러고 나니 break를 만나버린다... -> 그럼 그 다음 값들은
            # 비교 되기도 전에 탈출 돼서
            # 결국 최솟값만 출력되는... 그런 프로그램인 것 같다
            # (start_num에 30 last_num에 1 해보면 -1을 출력하는 걸 보니 그러한 듯)
            # 그리고 외부 for문으로 다시 돌아가서 다른 소수를 찾을 거라 생각했는데
            # 그건 아니고 바로 if total_num으로 넘어간다
            # why?? 아마 내부 for와 break가 소속된 조건문이 같은 선상에 있어서
            # 탈출할 위치가 아니기 때문인 듯 == 외부 for 자체를 나가니 순서대로 진행
if total_num == 0:
    print(-1)