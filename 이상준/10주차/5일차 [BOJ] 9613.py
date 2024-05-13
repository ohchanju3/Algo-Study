# GCD 합 ( https://www.acmicpc.net/problem/9613 )
# input : 정수와 숫자들 받아오기
import sys
input = sys.stdin.readline

# 두 수 의 GCD 합 구하는 함수
def GCD(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b
N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    num_of_nums = arr.pop(0)
    sum_ = 0
    for i in range(num_of_nums - 1):
        for j in range(i + 1, num_of_nums):
            sum_ += GCD(arr[i], arr[j])
    print(sum_)
