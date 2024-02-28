# 스택 ( https://www.acmicpc.net/problem/10828 )
# input : N과 N개의 문자열
import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        arr.append(order[1])

    elif order[0] == 'pop':
        try:
            print(arr[-1])
            arr.pop()
        except:
            print(-1)

    elif order[0] == 'size':
        print(len(arr))

    elif order[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    
    elif order[0] == 'top':
        try:
            print(arr[-1])
        except:
            print(-1)

'''
알게된 점
for문이 있고 loop가 10만개 이상이면
sys를 쓰자 
'''