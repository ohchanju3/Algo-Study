# 골드바흐의 추측 ( https://www.acmicpc.net/problem/6588 )
# input : 수들, 0이면 계산을 끝냄
# 일정 범위까지 에라토스테네스의 체 만드는 함수
import sys
input = sys.stdin.readline
def era(n):
    arr = [True for _ in range(n+1)]
    p = 2
    # n의 제곱근 범위까지 p를 올려가며 해당 arr내의 모든 소수가 아닌 index번호를 모두 False로 바꾼다.
    while (p*p <= n):
        if(arr[p] == True):
            for i in range(p*p, n+1, p):
                arr[i] = False
        p += 1
    return arr

# 소수 리스트 미리생성
MAX_N = 1000000
arr = era(MAX_N)

# 입력과 문제 해결 로직
while 1:
    inp = int(input())

    # 0입력 시 while문 나가기
    if inp == 0:
        break

    # 0이 아닌수이면 계산 시작
    for i in range(3, inp//2 + 1, 2): # 중요 : 애초에 3부터 시작하여 0,1,2에 대한 에라토스테네스 체 검증을 굳이 안해도 됨.
        if arr[i] and arr[inp-i]:
            print(f"{inp} = {i} + {inp-i}")
            break
    else: # for-else 구문
        print("Goldbach's conjecture is wrong.")


'''
<채점 결과 : 시간초과>
def sosu(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while 1:
    inp = int(input())
    if inp == 0:
        break
    found = False
    for i in range(inp, 1, -1):
        if sosu(i):
            for j in range(2, inp - i + 1):
                if sosu(j) and i + j == inp:
                    print(f"{inp} = {j} + {i}")
                    found = True
                    break
            if found:
                break  
    else: print("Goldbach's conjecture is wrong.")
'''

