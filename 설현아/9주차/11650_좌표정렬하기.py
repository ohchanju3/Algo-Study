N = int(input())
lst = []

for i in range(N):
  [x, y] = map(int, input().split())
  lst.append([x, y])

result = sorted(lst)

for i in range(N):
  print(result[i][0], result[i][1])