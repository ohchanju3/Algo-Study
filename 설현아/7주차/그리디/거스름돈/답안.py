import time


n = int(input())
result = []

coin_types = [500, 100, 50, 10]

start_time = time.time()

for coin in coin_types:
  result.append(n // coin)
  n %= coin

end_time = time.time()

print(result)
print(end_time - start_time)

# 소요시간 : 1.9