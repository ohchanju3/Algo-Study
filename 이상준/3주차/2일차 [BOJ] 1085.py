# 직사각형에서 탈출 ( https://www.acmicpc.net/problem/1085 )
# input x,y,w,h 받아오기
X, Y, W, H = map(int, input().split())

# 직사각형의 경계선까지 가는 거리의 최솟값을 구하자
output = min(X, Y, abs(X-W), abs(Y-H))
print(output)

'''
알게된 점
1. abs는 절댓값 함수
'''