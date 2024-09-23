x = int(input("first number: "))
y = int(input("second number: "))

if x > 0 and y > 0:
    print("Quadrant 1")
#     x, y 값이 모두 양수 = 제1사분면
elif x < 0 and y > 0:
    print("Quadrant 2")
#     x가 음수, y가 양수 = 제2사분면
elif x < 0 and y < 0:
    print("Quadrant 3")
#     x가 음수, y가 음수 = 제 3사분면
elif x > 0 and y < 0:
    print("Quadrant 4")
#     x가 양수, y가 음수 = 제4사분면
elif x == 0 or y == 0:
    print("in the line")
#     둘 중 한 값이 0이면 선에 존재