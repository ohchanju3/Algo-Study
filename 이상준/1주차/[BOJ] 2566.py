# 행렬 A를 입력받기 
A = []
for i in range(9):
    A.append(list(map(int, input().split())))

# 입력받은 행렬을 이용해서 최댓값과 최댓값의 위치 구하기
A_max = 0
for i in range(9):
    for j in range(9):
        if A_max <= A[i][j]:
            A_max = A[i][j]
            max_i = i+1
            max_j = j+1

# output
print(A_max)
print(max_i, max_j)

# 알게된 점
# 1. (주의) 인덱스 값은 0부터 시작이므로 좌표를 출력해야할 시 +1연산을 추가하여 출력하여야한다.
# 2. 행렬 입력받기 다시 확인하기