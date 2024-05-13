n = int(input())
time_list = list(map(int, input().split()))

time_list.sort()

result = 0
for i in range(0, len(time_list)):
  for j in range(0, i+1):
    result += time_list[j]

print(result)