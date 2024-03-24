# ROT13 ( https://www.acmicpc.net/problem/11655 )
# input 문자열 S
S = input()
output = ''
for i in range(len(S)):
    temp = S[i]
    if ord(temp) >= 65 and ord(temp) <= 90:
        encrypted_decimal_temp = ord(temp) + 13
        if encrypted_decimal_temp > 90:
            encrypted_decimal_temp = encrypted_decimal_temp - 26
        output += chr(encrypted_decimal_temp)
    elif ord(temp) >= 97 and ord(temp) <= 122:
        encrypted_decimal_temp = ord(temp) + 13
        if encrypted_decimal_temp > 122:
            encrypted_decimal_temp = encrypted_decimal_temp - 26
        output += chr(encrypted_decimal_temp)
    else: output += temp
print(output)