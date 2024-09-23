print("개수 입력:")
N = int(input())

print("숫자 입력: ")
numbers = []
for _ in range(N):
    numbers.append(int(input()))
# numbers라는 리스트에 input으로 받은 값들을 append 시킴

# for, if문을 써서 정렬시키던 부분
numbers_sorted = sorted(numbers)

for n in numbers_sorted:
    print(n)