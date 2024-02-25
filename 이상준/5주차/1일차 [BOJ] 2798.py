# 블랙잭 ( https://www.acmicpc.net/problem/2798 )
# 카드 개수 N, 목표 수 M, 카드에 써져있는 수 주어짐
N, M = map(int, input().split())
lst_card = list(map(int, input().split()))

# 합이 M을 넘지 않는 카드 3장을 찾기
int_max = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = lst_card[i]+lst_card[j]+lst_card[k]
            if (temp > int_max) & (temp <= M):
                int_max = temp

print(int_max)