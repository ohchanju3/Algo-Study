# 오등큰수 ( https://www.acmicpc.net/problem/17299 )
# input : N과 seq
import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))

count = [0] * 1000001
stack = []
output = [-1] * N

for i in range(N):
    count[seq[i]] += 1

for i in range(N):
    while stack and count[seq[i]] > count[seq[stack[-1]]]:
        output[stack.pop()] = seq[i]
    stack.append(i)

print(" ".join(map(str,output)))