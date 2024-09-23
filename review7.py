# number_list = list(int(input()))

# min max X 
number_list = list(map(int, input().split()))

# 초기 값 설정
# 초기 값 설정을 안 해 주면 파이썬은 자동으로 0을 설정
# 최솟값을 구하지 못하고 0만 나오는 문제 발생
maxNum = number_list[0]
minNum = number_list[0]

for i in number_list[1:]:
    if i > maxNum:
        maxNum = i
    elif i < minNum:
        minNum = i

print("최솟값은 %d, 최댓값은 %d입니다"%(minNum,maxNum))

# min max O
print("최솟값은 ",min(number_list),"최댓값은 ",max(number_list),"입니다")