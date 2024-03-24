# 문자열 분석 ( https://www.acmicpc.net/problem/10820 )
# N번째줄까지 input을 받고 연산
while 1:
    try:
        string = input()
        if not string:
            break
    except:
        break

    cnt = [0]*4
    for i in range(len(string)):
        if string[i] == ' ':
            cnt[3] += 1
        else:
            if ord(string[i]) >= 97 and ord(string[i]) <= 122:
                cnt[0] += 1
            elif ord(string[i]) >= 65 and ord(string[i]) <= 90:
                cnt[1] += 1
            else: cnt[2] += 1
    print(' '.join(map(str, cnt)))