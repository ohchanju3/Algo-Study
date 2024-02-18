# 백준 심화 단계

#25083
"""
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")
"""

# 3003
"""
correct = [1,1,2,2,2,8]
x = list(map(int,input().split()))

for i in range(0,len(correct)) :
  print(correct[i] - x[i], end=" ")
"""

# 2444
"""
n = int(input())
result = ""
for i in range(n-1,-1, -1):
  result += " "*i
  result += "*"*((n-i)+(n-i-1))
  result += "\n"
for i in range(1,n):
  result += " "*i
  result += "*"*((n-i)+(n-i-1))
  result += "\n"
print(result)
"""

# 10988
"""
x = input()
if x == x[::-1] :
  print(1)
else :
  print(0)
"""

# 1157
"""
word = input().upper()
word_list = list(set(word))
cnt_list = []
for i in word_list :
  cnt_list.append(word.count(i))
if cnt_list.count(max(cnt_list)) > 1 :
  print("?")
else:
  print(word_list[cnt_list.index(max(cnt_list))])
"""

# 2941
"""
alpabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
x = input()
result = ""
for i in alpabet :
  if x.find(i) >= 0 :
    x = x.replace(i,"x")
print(len(x))
"""

# 1316
"""
n = int(input())
cnt = 0
for i in range(n):
  word = input()
  for j in range(0, len(word)-1):
    if word[j] == word[j+1] :
      pass
    elif word[j] in word[j+1:]:
      cnt += 1
      break
print(n-cnt)
"""

# 25206
sum = 0
total = 0

for i in range(20):
  subject, credit, grade = input().split()

  if grade == "A+" :
    num_grade = 4.5
  elif grade == "A0" :
    num_grade = 4.0
  elif grade == "B+" :
    num_grade = 3.5
  elif grade == "B0" :
    num_grade = 3.0
  elif grade == "C+" :
    num_grade = 2.5
  elif grade == "C0" :
    num_grade = 2.0
  elif grade == "D+" :
    num_grade = 1.5
  elif grade == "D0" :
    num_grade = 1.0
  elif grade == "F" :
    num_grade = 0
  else: 
    continue
  sum += float(credit) * num_grade
  total += float(credit)
print(sum/total)