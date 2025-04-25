n,m = map(int,input().split(" "))
basket = [i+1 for i in range(n)]

for _ in range(m):
  i,j = map(int,input().split(" "))
  start=i-1
  end=j
  basket[start:end] = basket[start:end][::-1]


print(*basket)