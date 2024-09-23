(print("고정 비용, 대당 생산 비용, 판매 가격 입력"))
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    val = int(A // (C - B))
    print(val + 1)