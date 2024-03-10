# 스택 수열 ( https://www.acmicpc.net/problem/1874 )
# input : n, 수열
'''n = int(input())
stack, ans, find = [], [], True
now = 1
# 숫자 1부터 시작
for _ in range(n):
    num = int(input())

    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        find = False

# 정답 출력
if not find:
    print('NO')
else:
    for i in ans:
        print(i)'''

import sys

def solution():
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    s = []
    answer = []
    cur = 1
    for value in nums:
        while cur <= value:
            answer.append('+')
            s.append(cur)
            cur += 1
        if s.pop() != value:
            return "NO"
        answer.append('-')
    return '\n'.join(answer)


print(solution())