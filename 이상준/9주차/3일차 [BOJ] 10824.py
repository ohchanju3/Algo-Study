# 네 수 ( https://www.acmicpc.net/problem/10824 )
# input : 숫자 네 개
import sys
input = sys.stdin.readline

A,B,C,D = input().split()

# print test
# print(A,B,C,D)

# A,B를 붙인 수와 C,D를 붙인 수의 합
temp = A+B
temp_2 = C+D
print(int(temp) + int(temp_2))