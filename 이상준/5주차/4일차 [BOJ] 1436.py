# 영화감독 숌 ( https://www.acmicpc.net/problem/1436 )
# input N
N = int(input())

# N번째 종말의 수
start = 0
n = 0

while 1:
    if '666' in str(start):
        n = n + 1
    if n == N:
        output = start
        break
    start = start + 1

print(output)