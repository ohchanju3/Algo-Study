import time

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

nums.sort()

start_time = time.time() # 시간 복잡도 측정

while m > 0 :
  for _ in range(k):
    if m > 0 :
      result += nums[-1]
      m -= 1
    else :
      break

  if m > 0 :
    result += nums[-2]
    m -= 1
  else :
    break

end_time = time.time() # 시간 복잡도 측정

print(result)
print(end_time - start_time)

# 소요시간 : 2.9