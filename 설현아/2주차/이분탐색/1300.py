# 1300번: k번째 수

"""
# 아래 코드는 메모리 초과로 실패
N = int(input())
k = int(input())
B = []

for i in range(1, N+1) :
  for j in range(1, N+1) :
    B.append(i * j)

B.sort()
print(B[k])
"""

N = int(input())
k = int(input())

start, end = 0, N*N

while start <= end :
  mid = (start + end) // 2
  cnt = 0

  for i in range(1, N + 1):
    cnt += min(mid // i, N)
    
  if cnt >= k :
      end = mid - 1
      answer = mid
  else:
      start = mid + 1

print(answer)