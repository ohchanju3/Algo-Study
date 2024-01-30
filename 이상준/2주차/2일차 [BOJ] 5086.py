# 배수와 약수 ( https://www.acmicpc.net/problem/5086 )
# 약수와 배수 관계 구하는 함수
def relation(A, B):
    if B % A == 0: 
        output = "factor"
    elif A % B == 0:
        output = "multiple"
    else:
        output = "neither"
    return output 


# 0,0나올때까지 input A와 B에 대한 output 구하기 
while 1:
    A, B = map(int, input().split())
    if (A == 0 & B == 0):
        break

    print(relation(A, B))

# 알게된 점 : 따로없음. 다른 사람 문제 풀이 잘 보기 