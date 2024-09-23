a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
# 같은 눈이 두 개만 나오면...
# 세 개의 주사위 중 두 개가 같은 경우의 수를 모두 elif로 처리해야 함
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(100 + a * 100)
elif b == c:
    print(100 + b * 100)
else:
    print(max(a, b, c) * 100)