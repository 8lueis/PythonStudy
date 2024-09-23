# 0 0 입력 시 while문 탈출
# 그 외의 정수 -> 덧셈

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    #    가장 가까운 반복문을 나가라
    else:
        print(A + B)
