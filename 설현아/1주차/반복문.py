# 2739_백준
# n = int(input())

# for i in range(1,10) :
#   print(n, "*", i, "=", n*i)

# 10950_백준
# n = int(input())
# for i in range(n) :
#   a, b = map(int,input().split())
#   print(a+b)

# 8393_백준
# n = int(input())
# result = 0

# for i in range(1,n+1) :
#   result += i

# print(result)

# 25304_백준
# x = int(input())
# n = int(input())

# for i in range(n) : 
#   p, q = map(int, input().split())
#   x -= (p * q)

# if x == 0 :
#   print("Yes")
# else :
#   print("No")

# 25314_백준
# n = int(input())
# result = ""

# for i in range(int(n/4)) :
#   result += "long "

# result += "int"
# print(result)

# 15552_백준
# import sys

# n = int(input())
# for i in range(n) :
#   a, b = map(int,sys.stdin.readline().split())
#   print(a + b)

# 11021_백준
# import sys

# n = int(input())
# for i in range(1, n+1) :
#   a, b = map(int,sys.stdin.readline().split())
#   print("Case #"+str(i)+":",a+b)

# 11022_백준
# import sys

# n = int(input())
# for i in range(1, n+1) :
#   a, b = map(int,sys.stdin.readline().split())
#   print("Case #"+str(i)+": "+str(a)+" + "+str(b)+" =",a+b)

# 2438_백준
# n = int(input())
# for i in range(1, n+1) :
#   print("*"*i)

# 2439_백준
# n = int(input())
# for i in range(1, n+1) :
#   print(" " * (n-i) + "*" * i)

# 10952_백준
# a, b = map(int,input().split())

# while a != 0 and b != 0 :
#   print(a+b)
#   a, b = map(int,input().split())

# 10951_백준
while True :
  try:
    a, b = map(int,input().split())
    print(a+b)
  except:
    break