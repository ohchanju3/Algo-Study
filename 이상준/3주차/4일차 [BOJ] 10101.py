# 삼각형 외우기 ( https://www.acmicpc.net/problem/10101 )
# input 3개 받기
N = []
for i in range(3):
    N.append(int(input()))

# 삼각형의 종류 구별
def triangle(list_N):
    if sum(list_N) != 180:
        return 'Error'
    else:
        if len(set(list_N)) == 1:
            return 'Equilateral'
        elif len(set(list_N)) == 3:
            return 'Scalene'
        else:
            return 'Isosceles'

# output
print(triangle(N))