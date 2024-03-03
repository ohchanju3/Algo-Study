N, M = map(int, input().split())
card = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            sum = card[i] + card[j] + card[z]
            if sum <= M:
                result = max(result, sum)
                
print(result)