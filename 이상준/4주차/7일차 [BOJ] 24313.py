# 알고리즘 수업 - 점근적 표기 1 ( https://www.acmicpc.net/problem/24313 )
# input a_1, a_2, c, n_0 받아오기
a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())

if ((a_1*n_0+a_0 <= c*n_0)) and (a_1 <= c):
    output = 1
else:
    output = 0

print(output)

'''
알게된 것
1. 9~10번줄을 
output = 0으로 퉁쳤더니 오류가 났다
왜지.....?
'''