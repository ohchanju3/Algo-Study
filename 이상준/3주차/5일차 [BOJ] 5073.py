# 삼각형과 세 변 ( https://www.acmicpc.net/problem/5073 )

# 삼각형 판단
def triangle_def(lst_inp):
    if sum(lst_inp) <= 2*max(lst_inp):
        return 'Invalid'
    else:
        if len(set(lst_inp)) == 1:
            return 'Equilateral'
        elif len(set(lst_inp)) == 2:
            return 'Isosceles'
        else:
            return 'Scalene'

# input 1000을 넘지 않는 양의 정수 3개가 입력된다. 마지막줄은 0 0 0
while 1:
    lst_temp = list(map(int, input().split()))
    if sum(lst_temp) == 0:
        break
    print(triangle_def(lst_temp))