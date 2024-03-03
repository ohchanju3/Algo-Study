# 설탕 배달 ( https://www.acmicpc.net/problem/2839 )
# input N 받기
N = int(input())

# 봉지의 개수 구하기 
# 봉지의 개수는 많아봤자 N//3이다.
def test(N):
    count_break = True
    for count in range(1, N//3 + 1):
        for j in range(count+1):
            if j * 5 + (count-j) * 3 == N:
                return count
    return -1

print(test(N))

'''
같은 생각 더 잘 짠 함수
'''
def test_2(N):
    n = 0
    while N > 0:
        if N % 5 == 0:
            return n + N//5
        N = N - 3
        n = n + 1
    if N == 0:
        return n
    else: return -1

print(test_2(N))