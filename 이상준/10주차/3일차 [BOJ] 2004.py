# 조합 0의 개수 ( https://www.acmicpc.net/problem/2004 )
# input n, m

n, m = map(int, input().split())

def count_2_5_factorial(x):
    count_2 = 0
    count_5 = 0
    i = 2
    j = 5
    while i <= x:
        count_2 += x // i
        i *= 2
    while j <= x:
        count_5 += x // j
        j *= 5

    return count_2, count_5

count_2 = count_2_5_factorial(n)[0] - count_2_5_factorial(m)[0] - count_2_5_factorial(n-m)[0]
count_5 = count_2_5_factorial(n)[1] - count_2_5_factorial(m)[1] - count_2_5_factorial(n-m)[1]
print(min(count_2, count_5))