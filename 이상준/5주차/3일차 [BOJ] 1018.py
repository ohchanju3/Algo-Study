# 체스판 다시 칠하기 ( https://www.acmicpc.net/problem/1018 )
# input N, M, 체스판
N, M = map(int, input().split())
lst_chess = []
for i in range(N):
    lst_chess.append(list(*(input().split())))

# 8*8체스판의 왼쪽위가 X(X = 'W' or X = 'B')일때, 다시 색칠할 정사각형의 개수를 출력하는 함수
def count_when_X(lst, X):
    count = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if lst[i][j] != X:
                        count = count + 1
                else:
                    if lst[i][j] == X:
                        count = count + 1
            else:
                if j % 2 == 0:
                    if lst[i][j] == X:
                        count = count + 1
                else:
                    if lst[i][j] != X:
                        count = count + 1
    return count

# 체스판 자를 수 있는 모든 경우의 수로 자르고 최소 개수 세서 그 최소를 구하기
lst_count = []
for x in range(N-7):
    for y in range(M-7):
        temp_lst_chess = [row[y:y+8] for row in lst_chess[x:x+8]]
        count_when_W = count_when_X(temp_lst_chess, 'W')
        count_when_B = count_when_X(temp_lst_chess, 'B')
        lst_count.append(min(count_when_W, count_when_B))
print(min(lst_count))

'''
알게된 것
이중 배열의 특정 구역만 가져오는 슬라이싱은 두 가지 방법이 있다.
1. numpy 임포트하여 np.array형식으로 바꾼 후 arr[0:8, 0:8]로 가져오기
 - 그러나 numpy 임포트는 백준에서 지원하지 않는다.
2. numpy 없이 리스트 컴프리헨션으로 슬라이싱 하기
 => [row[0:8] for row in lst[0:8]]
 - 이 방법을 꼭 기억해야 앞으로 있을 리스트 자르기 문제에 대비할 수 있을듯하다

<생각해보기>
3차원배열도 자를 수 있을까?
=> [[dim3[0:2] for dim3 in dim2[0:2]] for dim2 in lst[0:2]]
굿굿
'''