# 연산자 끼워넣기 ( https://www.acmicpc.net/problem/14888 )
# input : N 과 숫자 그리고 연산자
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

# 연산의 최댓값과 최솟값을 구하는 법 : 모든 상황을 계산한다.
out_min = 0
out_max = 0

# 여기선 각ops의 개수가 주어진다. 그리고 총 개수도 N-1로 일정하다.
# 숫자의 개수가 N으로 주어진다.
# 1. 각 숫자를 가져와 계산하기 vs 2. 각 ops를 가져와 계산하기 이를 테면 2,3,1,4개면 경우의수가 10C2 * 8C3 * 5C1 * 4C4임.

while sum(ops) > 0:
    # 모종의 계산 과정을 통해 nums와 ops를 계산
    if temp_res >= out_max:
        out_max = temp_res
    if temp_res <= out_min:
        out_min = temp_res
    
    