# 후위 표기식 ( https://www.acmicpc.net/problem/1935 )
# input N 과 후위 표기식
import sys
input = sys.stdin.readline
N = int(input())
inp = input().strip()
stack = []
dic = {}


# # input test 용 코드
# print(N, inp, type(inp))

# dic에 서로다른 문자에 대한 value 저장하기
for i in range(65, 65+N):
    temp = chr(i)
    dic[temp] = int(input())

# # dic test 용 코드
# print(dic)

for i in range(len(inp)):
    temp = inp[i]
    # temp가 기호인 경우
    if temp == '+':
        stack.append(stack.pop() + stack.pop())
    elif temp == '-':
        stack.append(- stack.pop() + stack.pop())
    elif temp == '*':
        stack.append(stack.pop() * stack.pop())
    elif temp == '/':
        stack.append(1/stack.pop() * stack.pop())
    # temp가 문자인 경우
    else:
        stack.append(dic[temp])

print(f'{stack[0]:.2f}')