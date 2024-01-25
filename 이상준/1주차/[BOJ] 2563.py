# 색종이 ( 참고 : https://www.acmicpc.net/problem/2563 )

# input 받기
n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

# 빈 도화지 2차원 배열 만들기
paper = [[0 for w in range(100)] for h in range(100)]

# i는 x좌표 j는 y좌표, 픽셀별로 검은색 색종이가 있나 계산
for i in range(1, 100+1):
    for j in range(1, 100+1):
        # 색종이 배열 불러오기
        for k in range(n):
            # 각 픽셀이 각 색종이 안에 있나 비교
            if A[k][0] <= i < A[k][0]+10 and A[k][1] <= j < A[k][1]+10:
                # 하나라도 있으면 1로 바꿈
                paper[j][i] = 1

# output ( 총 도화지에 올라간 1*1 픽셀의 개수 구하기 )
cnt = 0
for i in range(100):
    cnt += paper[i].count(1)
print(cnt)

# idea1 : ABC 합집합 = A + B + C - (A교B + B교C + C교A) + A교B교C -> 실패
# idea2 : 도화지 픽셀당 계산하여 그 값 더하기 -> 성공