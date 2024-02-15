# 세 막대 ( https://www.acmicpc.net/problem/14215 )
# input a,b,c
lst_abc = list(map(int, input().split()))

'''
삼각형은 (가장 긴변의 길이) < 나머지 두 변의 길이의 합.
이 말은 즉, (가장 긴변의 길이)*2 < 모든 변의 길의 합.

따라서 a, b, c가 주어졌을 때 가장 긴 막대를 찾은 후
막대들은 최대한 자르지 않는 쪽으로 연산하여야한다.
'''

# 삼각형의 조건을 만족하는 경우
if 2*max(lst_abc) < sum(lst_abc):
    output = sum(lst_abc)
# 만족하지 않는 경우
else:
    output = 2*(sum(lst_abc) - max(lst_abc)) - 1

print(output)