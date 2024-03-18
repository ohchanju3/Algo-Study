import time


n, m = map(int, input().split())
table = []
max_num = 0

start_time = time.time() # 시간 복잡도 측정

for _ in range(n):
  row = list(map(int, input().split()))
  table.append(row)

for row in table:
  if max_num < min(row):
    max_num = min(row)
    
end_time = time.time() # 시간 복잡도 측정

print(max_num)
print(end_time - start_time)

# 소요시간 : 0.34