# 최대공약수와 최소공배수 ( https://www.acmicpc.net/problem/2609 )
# input : A,B 두 개의 수
A, B = map(int, input().split())
# 최대공약수
for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        print(i)
        break

# 최소공배수
for i in range(1, max(A,B)+1):
    if i * min(A,B) % max(A,B) == 0:
        print(i * min(A,B))
        break