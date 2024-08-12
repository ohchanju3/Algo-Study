a, b = map(int, input().split())

result = a - b

if result > 0 :
  print(">")
elif result < 0 :
  print("<")
else :
  print("==")