# 소수 찾기 ( https://www.acmicpc.net/problem/1978 )
# input N과 N개의 수 받아오기
N = int(input())
N_list = list(map(int, input().split()))

# 소수인지 판단
def is_it_deciaml(N):
    ret = True
    if N == 1:
        return False
    for i in range(2, N//2 + 1):
        if N % i == 0:
            ret = False
            break
    return ret

# output 출력
output = 0
for i in N_list:
    if is_it_deciaml(i) == True:
        output = output + 1
print(output)