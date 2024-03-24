n = int(input())
cnt = 0
end = 666

while True:
  if '666' in str(end):
    cnt += 1
    
  if cnt == n:
    break

  end += 1

print(end)