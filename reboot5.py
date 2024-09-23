x = int(input())

y = int(input())

if x > 0 and y > 0:
    print("제 1사분면")
elif x < 0 and y > 0:
    print("제 2사분면")
elif x < 0 and y < 0:
    print("제 3사분면")
elif x > 0 and y < 0:
    print("제 4사분면")
elif x == 0 or y == 0:
    print("선 위에 존재")