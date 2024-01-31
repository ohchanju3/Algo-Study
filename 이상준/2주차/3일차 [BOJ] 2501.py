# 약수 구하기 ( https://www.acmicpc.net/problem/2501 )
# input N, K 받아오기 
N, K = map(int, input().split())

# 약수를 빈 리스트로 선언
yaksu = []
# N/2 보다 작은 범위에서 약수 구하기 
for i in range(1, int(N/2)+1):
    if N % i == 0:
        yaksu.append(int(i))

# 약수에 자기자신 추가하기
yaksu.append(N)

# output : 약수중 K번째로 작은 수를 출력
# 단, N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우 0 출력
if len(yaksu) < K:
    print("0")
else:
    print(yaksu[K-1])