'''
내 초기 답
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
    
못 품 답 봄
'''

# input 입력받기 
n = int(input())
# 수열 입력받기 
data = list(map(int, input().split()))
# 연산자 개수 입력받기
add, sub, mul, div = map(int,input().split())

# 최댓값과 최솟값 초기화 : 최소 -10억, 최대 10억
max_value = int(-1e9)
min_value = int(1e9)
print("===================")
# dfs 메서드 정의
def dfs(i, num):
    global add, sub, mul, div, max_value, min_value
    # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
    if i == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
    else:
        # i가 n보다 작은 경우 ( 한참 게산중인 경우 )
        if add > 0:
            add -= 1
            dfs(i+1, num + data[i]) # 재귀
            add += 1 # 재귀 다 끝나고 add 개수 복구
        if sub > 0:
            sub -= 1
            dfs(i+1, num - data[i]) # 재귀
            sub += 1 # 재귀 끝나고 sub 개수 복구
        if mul > 0:
            mul -= 1
            dfs(i+1, num * data[i]) # 재귀
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(num / data[i])) # 재귀, 나눗셈은 정수로 바꿈
            div += 1
# dfs 메서드 호출
dfs(1, data[0]) # 시작 인덱스는 1이고 시작 숫자는 받은 숫자 배열의 첫번째놈
# 최댓값과 최솟값 출력
print(max_value)
print(min_value)