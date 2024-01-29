# 중앙이동 알고리즘  https://www.acmicpc.net/problem/2903
# input N 받아오기
N = int(input())

# 상근이는 점 4개를 고른다.
temp = 2

# 정사각형의 각 변의 중앙에 점을 하나 추가한다.
for i in range(N):
    temp += 2**i

# 한변의 제곱 = 점의 개수
output = temp**2

# output : 점 개수 출력
print(output)

# 알게된 것
# ?? 이렇게 푸는게 맞나? 맞았다.
# 알고리즘의 탈을 쓴 그냥 수학 수열 문제