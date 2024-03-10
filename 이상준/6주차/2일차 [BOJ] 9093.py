# 단어 뒤집기 ( https://www.acmicpc.net/problem/9093 )
# input : 문장 개수, 문장
import sys
n = int(sys.stdin.readline())
for i in range(n):
    arr = sys.stdin.readline().split()
    for word in arr:
        temp = ''
        for j in range(len(word)):
            target = j + 1
            temp = temp + word[-target]
        print(temp, end = ' ')
    print()

'''
다른 풀이
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    statement = input().split()
    print(statement[::-1])
    # ['today', 'happy', 'am', 'I']
    print(' '.join(statement[::-1]))
    # today happy am I
    print(' '.join(statement[::-1])[::-1])
    # I ma yppah yadot
'''