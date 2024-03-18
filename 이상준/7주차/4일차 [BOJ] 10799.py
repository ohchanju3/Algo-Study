# 쇠막대기 ( https://www.acmicpc.net/problem/10799 )
# input : 괄호 받아오기 sting 형태로
import sys
input = sys.stdin.readline
S = input().strip()

stack = []
count = 0
# 문자 하나하나 골라서 테스트
for i in range(0, len(S)):
    # 만약 뽑은 문자가 '('라면, 그냥 스택에 추가한다
    if S[i] == '(':
        stack.append('(')
    # 만약 뽑은 문자가 ')'라면, 바로 앞전의 기호에 따라 다른 연산을 한다.
    else:
        # 만약 ')' 바로 전에 '(' 기호가 있었다면, 레이저 쏘기 이므로 pop한번하고(레이져쏘고) 스택에 남아있는 '(' 개수만큼 막대가 생성된다.
        if S[i-1] == '(':
            stack.pop()
            count += len(stack)
        # 만약 ')' 바로 전에 또 ')' 기호가 있었다면, 자르는 막대가 하나 준 것이므로 pop한번 하고 막대 개수에 1을 더하고 스택에서 '('하나를 뺀다.
        else:
            stack.pop()
            count += 1
print(count)