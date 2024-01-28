# 세탁소 사장 동혁 ( https://www.acmicpc.net/problem/2720 )
# input 테스트 케이스의 개수 T, 각 테스트 케이스의 거스름돈 C(센트)
T = int(input())
C = []
for i in range(T):
    C.append(int(input()))

# 잔돈을 계산하는 함수
def coin(x):
    lst_res = [0, 0, 0, 0]
    while x != 0:
        if x >= 25:
            lst_res[0] = x // 25
            x = x % 25
        elif x >= 10:
            lst_res[1] = x // 10
            x = x % 10
        elif x >= 5:
            lst_res[2] = x // 5
            x = x % 5
        else:
            lst_res[3] = x
            x = x % 1
    return lst_res

# output : 테스트 케이스의 개수 T줄만큼 동전 개수 출력
for c in C:
    for i in coin(c):
        print(i, end = ' ')
    print()