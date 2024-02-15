# 대지 ( https://www.acmicpc.net/problem/9063 )
# N, 점의 x좌표들, y좌표들 각각 input으로 받기 
N = int(input())
x = []; y = []
for i in range(N):
    x_temp, y_temp = map(int, input().split())
    x.append(x_temp); y.append(y_temp)

# 대지의 최소 넓이 구하기
width = max(x)-min(x)
height = max(y)-min(y)
area = width*height
print(area)