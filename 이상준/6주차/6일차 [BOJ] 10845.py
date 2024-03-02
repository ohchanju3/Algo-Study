# 큐 ( https://www.acmicpc.net/problem/10845 )
# input : 명령의 수, 명령어 및 수
import sys
input = sys.stdin.readline
n = int(input())
que = []

for _ in range(n):
    command = input().split()
    if command[0] == 'push': que.append(command[1])
    elif command[0] == 'pop': print(que.pop(0) if que else -1)
    elif command[0] == 'size': print(len(que))
    elif command[0] == 'empty': print(0 if que else 1)
    elif command[0] == 'front': print(que[0] if que else -1)
    else: print(que[-1] if que else -1)
    
'''
# 첫번째 시도 : 큐의 pop(0) 연산이 많이 들것 같아서 했으나.. 이게 왠걸 걍 pop쓰는게 시간이 단축되었음
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
que = deque()

def operation(command):
    global que
    if command[0] == 'push':
        que.append(command[1])
        return
    elif command[0] == 'pop':
        if que:
            print(que.popleft())
        else: print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if que:
            print(0)
        else: print(1)
    elif command[0] == 'front':
        if que:
            print(que[0])
        else: print(-1)
    elif command[0] == 'back':
        if que:
            print(que[-1])
        else: print(-1)

for _ in range(n):
    command = input().split()
    operation(command)
'''

