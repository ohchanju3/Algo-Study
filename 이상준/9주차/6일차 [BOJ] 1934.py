# 최소공배수 ( https://www.acmicpc.net/problem/1934 )
# input : N줄의 2쌍의 수
import sys
input = sys.stdin.readline

def gongbaesu(A, B):
    big = max(A, B)
    small = min(A, B)
    if big % small == 0:
        print(big)
        return
    else:
        for i in range(1, big + 1):
            if small * i % big == 0:
                print(small * i)
                break
    return

N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    gongbaesu(A,B)

'''
import sys

T=int(input())

for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    aa,bb=a,b

    while a%b!=0:
        a,b = b,a%b
 40 6 = 6, 4
 6 4 = 4, 2

 40*6//2 = 240ㅅㅂ 이게 왜 됨.....?
 최대 공약수 = ? a?

 30 40 = 40 30
 40 30 = 30 10

 30*40 // 10 = 120

    print(aa*bb//b)
'''