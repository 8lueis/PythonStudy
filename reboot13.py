print("개수 입력:")
N = int(input())

print("숫자 입력: ")
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# Bubble Sort
# i가 한 바퀴 돌 때 j가 5바퀴(0, 1, 2, 3, 4) 돌아가는 반복문
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            # 현재 원소(numbers[i])가 이전 원소(numbers[j])보다 작으면
            # j 위치의 값이 i 위치의 값보다 작으면 (94, 10 -> true)
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # j는 i의 위치로, i는 j의 위치로 (10, 94로 변경)

for n in numbers:
    print(n)
