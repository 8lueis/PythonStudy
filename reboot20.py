def s3(n):
    a = []
    s = str(n)
    s = reversed(s)
    # n -> int 값
    # s -> n의 str 값
    for i in s:
        a.append(int(i))

    return a

print("숫자 입력: ")
num = int(input())
result = s3(num)
print(result)