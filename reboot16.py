# def factorial(num):
#     result = 1
#     if num > 0:
#         # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#         result = num * factorial(num - 1)
#         return result
#
# print("숫자 입력")
# n = int(input())
# print(factorial(n))

def factorial(num):
    if num == 0:
        return 1 # 0 팩토리얼은 1...
    else:
        result = num * factorial(num - 1)
        return result

print("숫자 입력")
n = int(input())
print(factorial(n))