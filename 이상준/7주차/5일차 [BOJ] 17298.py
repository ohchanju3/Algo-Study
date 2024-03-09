# 오큰수 ( https://www.acmicpc.net/problem/17298 )
# input : N과 수 받아오기
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
temp = max(nums)
output = []

for i in range(N):
    if i == N - 1 or nums[i] == temp:
        output.append('-1')
    else:
        for j in range(i+1, N):
            if nums[j] > nums[i]:
                output.append(str(nums[j]))
                break
        else: output.append('-1')
print(' '.join(output))