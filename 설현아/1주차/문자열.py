# 백준 5단계 문자열

# 27866
"""
word = input()
n = int(input())
print(word[n-1])
"""

# 2743
"""
word = input()
print(len(word))
"""

# 9086
"""
n = int(input())
for i in range(n):
  word = input()
  print(word[0]+word[-1])
"""

# 11654
"""
x = input()
print(ord(x))
"""

# 11720
"""
n = int(input())
number = input()
sum = 0

for i in range(n):
  sum += int(number[i])

print(sum)
"""

# 10809
"""
word = input()
for i in range(97,123):#chr(i)
  if chr(i) in word:
    print(word.index(chr(i)), end=" ")
  else: print("-1", end=" ")
"""

# 2675
"""
n = int(input())
result = ""
for i in range(n):
  times, string = map(str,input().split())
  for j in range(len(string)):
    result += string[j] * int(times)
  result += "\n"
print(result)
"""

# 1152
"""
sentence = input()
word_list = list(sentence.split())
print(len(word_list))
"""

# 2908
"""
sentence= list(input().split())
sentence[0] = sentence[0][::-1]
sentence[1] = sentence[1][::-1]
sentence[0] = int(sentence[0])
sentence[1] = int(sentence[1])
print(max(sentence))
"""

# 5622
"""
word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for j in range(len(word)):
    for i in dial:
        if word[j] in i:
            result += dial.index(i)+3
print(result)
"""

# 11718
"""
while True:
  try: 
    x = input()
    print(x)
  except EOFError: 
    break
"""