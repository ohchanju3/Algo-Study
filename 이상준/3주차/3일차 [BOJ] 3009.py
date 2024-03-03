# 네 번째 점 ( https://www.acmicpc.net/problem/3009 )
# input : 세 점의 좌표가 한줄에 하나씩 주어짐
int_x = []
int_y = []
for i in range(3):
    x, y = map(int, input().split())
    int_x.append(x)
    int_y.append(y)

# 직사각형을 만들기 위해 필요한 네번째 점을 찾는 프로그램 작성
for i in range(3):
    if int_x.count(int_x[i]) == 1:
        output_x = int_x[i]
    if int_y.count(int_y[i]) == 1:
        output_y = int_y[i]
print(output_x, output_y)

'''
동일한 메커니즘, 더 효율적인 문법

x = []
y = []

def rule(L,N):
    if N not in L:
        L.append(N)
    else:
        L.remove(N)
# 이렇게 하면 결국에 남는 건 개수가 하나인 인수

for i in range(3):
    a,b = map(int, input(),split())
    rule(x, a)
    rule(y, b)
print(x[0], y[0])
'''