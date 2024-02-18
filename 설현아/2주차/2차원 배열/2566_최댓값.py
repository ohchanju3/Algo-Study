max_num, row, col = 0, 0, 0
row = []

for i in range(1, 10):
  row = list(map(int,input().split()))
  if max(row) > max_num :
    max_num = max(row)
    row = i + 1
    col = row.index(max_num) + 1

print(max_num)
print(row, col)