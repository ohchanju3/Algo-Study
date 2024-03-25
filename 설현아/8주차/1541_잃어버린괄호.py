nums_string = input() #55-50+40
num_lst = list(map(str, nums_string.split("-")))

for i in range(len(num_lst)):
  if num_lst[i].find("+") != -1:
    plus = list(map(int, num_lst[i].split("+")))
    num_lst[i] = sum(plus)

result = int(num_lst[0])
if len(num_lst) > 1:
  for i in range(1,len(num_lst)):
    result -= int(num_lst[i])

print(result)

