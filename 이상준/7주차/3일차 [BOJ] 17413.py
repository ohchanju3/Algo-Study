# 단어 뒤집기 2 ( https://www.acmicpc.net/problem/17413 )
# input 수열 S
import sys
input = sys.stdin.readline
S = input().strip().split('<')
arr = [word.split('>') for word in S]

output = ''
for value in arr:
    if len(value) == 2:
        output = output + '<' + value[0] + '>'
        temp = value[1].split()

        for i in range(len(temp)):
            output = output + temp[i][::-1]
            if i != len(temp) - 1:
                output += ' '
    else:
        temp = value[0].split()

        for i in range(len(temp)):
            output = output + temp[i][::-1]
            if i != len(temp) - 1:
                output += ' '
            

print(output)