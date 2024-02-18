# 1330_백준
# A,B = map(int,input().split())
# if A>B :
#   print(">")
# if A<B :
#   print("<")
# if A==B :
#   print("==")

# 9498_백준
# A=int(input())//10
# if A>=9 : 
#   print("A")
# elif A>=8 and A<9 :
#   print("B")
# elif A>=7 and A<8 :
#   print("C")
# elif A>=6 and A<7 :
#   print("D")
# else :
#   print("F")

# 2753_백준
# A = int(input())
# if ((A%4==0 and A%100!=0) or A%400==0):
#   print(1)
# else: 
#   print(0)

# 14681_백준
# x = int(input())
# y = int(input())

# if x>0 and y>0 :
#   print(1)
# if x<0 and y>0 :
#   print(2)
# if x<0 and y<0 :
#   print(3)
# if x>0 and y<0 :
#   print(4)

# 2884_백준
# H, M = map(int, input().split())

# if M<45 :
#   if H==0 :
#     H=23
#   else:
#     H-=1  
#   M=M+60-45
#   print(H, M)
# else :
#   print(H, M-45)

# 2525_백준
# H, M = map(int, input().split())
# X = int(input())

# H += X // 60
# M += X % 60

# if M >= 60 :
#   M -= 60
#   H += 1
# if H >= 24 :
#   H -= 24

# print(H, M)

# 2480_백준
X, Y, Z = map(int, input().split())

if X == Y == Z :
  result = X * 1000 + 10000

elif X == Y or X == Z :
  result = X * 100 + 1000

elif Y == Z :
  result = Y * 100 + 1000

else :
  result = max(X,Y,Z) * 100

print(result)