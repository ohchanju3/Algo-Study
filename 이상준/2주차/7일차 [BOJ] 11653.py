# 소인수분해 ( https://www.acmicpc.net/problem/11653 )
# input N 받기
N = int(input())

# 소인수 분해
while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N = N // i
            break