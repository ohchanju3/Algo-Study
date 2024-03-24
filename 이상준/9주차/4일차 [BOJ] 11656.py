# 접미사 배열 ( https://www.acmicpc.net/problem/11656 )
# input : S
S = input()

suffix = []

for i in range(len(S)):
    suffix.append(S[i:])

for suf in sorted(suffix):
    print(suf)