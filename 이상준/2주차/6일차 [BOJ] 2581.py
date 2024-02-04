# 소수 ( https://www.acmicpc.net/problem/2581 )
# input M, N받아오기 ( M > N )
M = int(input())
N = int(input())

# N이 소수면 True, 아니면 False를 반환
def is_it_decimal(N):
    if N == 1:
        return False
    for i in range(2, N//2 +1):
        if N % i == 0:
            return False
    return True

# M이상, N이하의 자연수 중 소수인 것을 모두찾기
ret_lst = [i for i in range(M, N+1) if is_it_decimal(i)]

# 합과 가장 작은 수 출력 단, 소수가 없으면 -1 출력
try:
    ret = ret_lst[0]
    print(sum(ret_lst))
    print(ret)
except IndexError:
    print(-1)

'''
알게된 것
1. try except구문 잘 쓰는법
2. 파이썬 스타일 코드짜는 법
'''