N = int(input())
temp_list = [[0] * 100 for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(b, b + 10):
        for j in range(a, a + 10):
            temp_list[i][j] = 1

result = 0
for k in range(100):
    result += temp_list[k].count(1)

print(result)