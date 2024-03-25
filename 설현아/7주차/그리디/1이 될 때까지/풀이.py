import time


n, k = map(int, input().split())
cnt = 0

start_time = time.time() # 시간 복잡도 측정

while n > 1:
  cnt += 1
  if n%k == 0:
    n = n/k
  else:
    n -= 1

end_time = time.time() # 시간 복잡도 측정

print(cnt)
print(end_time - start_time)

# 소요시간 : 1.59