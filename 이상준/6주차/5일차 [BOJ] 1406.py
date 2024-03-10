# 에디터 ( https://www.acmicpc.net/problem/1406 )
# input : 현재 상태, M, 문자열들

import sys
start_stack = list(input())
num_of_command = int(input())
temp_stack = []

# 특징 1 : stack 2개를 이용하여 del이나, insert를 쓰지 않아 계산 시간을 줄임
def editor(command):
    global start_stack, temp_stack

    if command[0] == 'L':
        try:
            temp_stack.append(start_stack.pop())
        except: return

    elif command[0] == 'D':
        try:
            start_stack.append(temp_stack.pop())
        except: return
    
    elif command[0] == 'B':
        try:
            start_stack.pop()
        except: return
    
    else:
        start_stack.append(command[1])

for num in range(num_of_command):
    command = sys.stdin.readline().split()
    editor(command)

# 특징 2 : temp_stack의 경우 뒤집어서 붙여야 본래 문자열이 반환됨. 뒤집어진 스택이기 때문.
output = ''.join(start_stack + temp_stack[::-1])
print(output)

'''
1차 시도 : 시간 초과
import sys
start_arr = list(input())
num_of_command = int(input())
current_cursor = len(start_arr)

def editor(command):
    global start_arr, current_cursor
    
    if command[0] == 'L':
        if current_cursor <= 0:
            return
        current_cursor = current_cursor - 1
    
    elif command[0] == 'D':
        if len(start_arr) <= current_cursor:
            return
        current_cursor = current_cursor + 1
    
    elif command[0] == 'B':
        if current_cursor <= 0:
            return
        del start_arr[current_cursor - 1]
        current_cursor = current_cursor - 1
    
    else:
        if len(start_arr) > current_cursor:
            start_arr.insert(current_cursor, command[1])
        else: 
            start_arr.append(command[1])
        current_cursor = current_cursor + 1
        return
    
    return

for num in range(num_of_command):
    command = sys.stdin.readline().split()
    print(command)
    editor(command)
print(''.join(start_arr))
'''
