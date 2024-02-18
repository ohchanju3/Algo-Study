n = int(input())

for _ in range(n):
	result = int(input())
	for i in [25, 10, 5, 1]:
		print(result // i, end=' ')
		result = result % i