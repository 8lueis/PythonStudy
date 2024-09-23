def s5(a,b):
    if a < b:
        toList = list(range(a, b+1))
        print("첫 번째 숫자 < 두 번째 숫자인 경우의 toLsit ==> ",toList)
        return sum(toList)
    else:
        toList = list(range(b, a+1))
        print("두 번째 숫자 < 첫 번째 숫자인 경우의 toLsit ==> ",toList)
        return sum(toList)

print("첫 번째 숫자")
num1 = int(input())

print("두 번째 숫자")
num2 = int(input())

result = s5(num1, num2)
print(result)