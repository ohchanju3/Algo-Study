# 알파벳 개수 ( https://www.acmicpc.net/problem/10808 )
# input S
S = str(input())
alphabet = [0]*26
for i in range(len(S)):
    temp = S[i]
    alphabet[ord(temp) - 97] += 1
print(' '.join(map(str, alphabet)))