
# while True:
#     A = int(input("첫 번째 값 입력: "))
#     B = int(input("두 번째 값 입력: "))
#
#     if A == 0 and B == 0:
#         break
#     else:
#         print(A + B)

while True:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		continue
	else:
		print(a+b)