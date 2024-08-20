n, m= map(int,input().split()) # n은 바구니 수, m은 공의 개수

basket=[0]*(n+1)

for _ in range(m):
  i,j,k = map(int,input().split())
  for x in range(i, j+1):
    basket[x] = k

for p in range(1,n+1):
  print(basket[p], end=' ')