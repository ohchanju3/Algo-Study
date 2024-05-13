# 소수 구하기 ( https://www.acmicpc.net/problem/1929 )
# input : 처음수와 마지막 수
import math
A, B = map(int, input().split())

# A 부터 B까지 소수면 출력 아니면 건너뛰는 함수
def f(i):
    if i == 1:
        return
    elif i == 2 or i == 3:
        print(i)
        return
    
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            return
    else: 
        print(i)
        return

for i in range(A, B+1):
    f(i)