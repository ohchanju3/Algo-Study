x, y = [], []
result_x, result_y = 0, 0
for _  in range(3):
  new_x, new_y = map(int, input().split())
  x.append(new_x)
  y.append(new_y)

for i in range(3):
  if x.count(x[i]) == 1:
    result_x = x[i]
  if y.count(y[i]) == 1:
    result_y = y[i]

print(result_x, result_y)