# 백준 2차원 배열

# 2738
N,M = map(int, input().split())
A, B=[], []

for _ in range(N) :
  A.append(list(map(int,input().split())))

for _ in range(N) :
  B.append(list(map(int,input().split())))

for i in range(0,N) :
  for j in range(0,M):
    print(A[i][j]+B[i][j], end=" ")
  print()
  # print("\n")
