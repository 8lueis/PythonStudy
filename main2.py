N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(N): # N개의 값을 가지게 되는 A 리스트
	if A[i] < X:
		print(A[i], end=" ")