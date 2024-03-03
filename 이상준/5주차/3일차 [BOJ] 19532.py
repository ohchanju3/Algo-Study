# 수학은 비대면강의입니다 ( https://www.acmicpc.net/problem/19532 )
# input a,b,c,d,e,f
a,b,c,d,e,f = map(int, input().split())

# 연립방정식의 해 : a*e - b*d는 문제의 조건에 의해 0이되지 않는다.
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# 정수로 출력
print(int(x), int(y))

'''
브루트 포스로 풀기

a,b,c,d,e,f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            print(i, j)
'''