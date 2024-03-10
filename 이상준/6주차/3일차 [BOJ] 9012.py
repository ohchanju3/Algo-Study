# 괄호 ( https://www.acmicpc.net/problem/9012 )
# input : 숫자와 문자열
import sys
n = int(sys.stdin.readline())

def yes_or_no(inp):
    temp = []
    for j in inp:
        # 각 기호에 대하여 j가 '(' 면 temp에 '('를 추가한다.
        if j == '(':
            temp.append('(')
        
        # 각 기호에 대하여 j가 ')' 면 temp 스택의 가장 뒤의 '('를 뺀다.
        elif j== ')':
            try:
                temp.pop()
            except:
                return 'NO'
    if temp:
        return 'NO'
    return 'YES'

for i in range(n):
    inp = sys.stdin.readline()
    print(yes_or_no(inp))

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     s = input().strip()
#     print(s)
#     while '()' in s:
#         s = s.replace('()','')
#     print('NO') if s else print('YES')