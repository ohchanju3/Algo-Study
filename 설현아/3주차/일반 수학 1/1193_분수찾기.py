'''
1 -> 2
2,3 -> 3
4,5,6 -> 4
7,8,9,10 -> 5
11,12,13,14,15 -> 6
=> n-1 개
'''

'''
X = int(input())
cnt, n = 1, 1 # n: 한 줄의 대각선에 위치한 요소 갯수
row, col = 1, 1

while cnt < X :
  if (n % 2 == 0 and col == 1) or (n % 2 == 1 and row == 1): # 짝수 줄
    n += 1
  if row + col -1 == n :
    if n % 2 == 0 : # 짝수 줄
      col -= 1
      row += 1
    else : # 홀수 줄
      col += 1
      row -= 1
    cnt += 1

  else :
    if n % 2 == 0 : # 짝수 줄
      col += 1
    else : # 홀수 줄
      row += 1
    cnt += 1

print(row , "/" , col)
'''

# 위의 풀이는 시간 초과로 실패

X = int(input())
n = 1

while X > n :
    X -= n
    n += 1
    
if n % 2 == 0 :
    a = X
    b = n - X + 1
else:
    b = X
    a = n - X + 1
    
print(str(a)+'/'+str(b))