# 팩토리얼 0의 개수 ( https://www.acmicpc.net/problem/1676 )
# input : N
N = int(input())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def zero_count(num, count = 0):
    if num % 10 != 0:
        return count
    else:
        count += 1
        return zero_count(num // 10, count)
    
print(zero_count(factorial(N)))