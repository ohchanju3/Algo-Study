n, m = map(int, input().split())

chess = []
for _ in range(n):
  chess.append(input())

cnt = 0
for i in range(len(chess)):
  if i>0 and chess[i-1][0] == chess[i][0]:
    cnt += 1
    if chess[i-1][0] == 'W':
      chess[i][0] = 'B'
    else:
      chess[i][0] = 'W'

  for j in range(1,len(chess[i])):
    if chess[i][j-1] == chess[i][j]:
      cnt += 1
      if chess[i][j-1] == 'W':
        chess[i][j] = 'B'
      else:
        chess[i][j] = 'W'

print(cnt)
