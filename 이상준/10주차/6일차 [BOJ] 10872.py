# 팩토리얼 ( https://www.acmicpc.net/problem/10872 )
# input : N
N = int(input())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(N))