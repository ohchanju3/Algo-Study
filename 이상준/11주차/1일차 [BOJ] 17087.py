# 숨바꼭질 6 ( https://www.acmicpc.net/problem/17087 )
# input : N, S

import sys

# input 대신 직접 값을 입력받는 부분을 사용하여 예시로 드립니다.
N, S = map(int, input().split())
arr = list(map(int, input().split()))

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 모든 위치와 S 사이의 거리 계산
for i in range(N):
    arr[i] = abs(arr[i] - S)

# 모든 거리의 GCD 계산
gcd = arr[0]
for i in range(1, N):
    gcd = GCD(gcd, arr[i])

print(gcd)
