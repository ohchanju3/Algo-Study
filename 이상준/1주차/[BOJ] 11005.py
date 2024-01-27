# 진법 변환 2 ( https://www.acmicpc.net/problem/11005 )
# N, B 받아오기
inp_N, inp_B = map(int, input().split())

# output 초기 설정
lst_output = []
temp = inp_N

# N이 0이 될때까지 나머지 비교 후 loop의 마지막에 N을 B로 나누고 나머지 버린값을 N에 넣기
while temp != 0:
    if temp % inp_B < 10:
        str_num = str(temp % inp_B)
        lst_output.insert(0, str_num)
        
    else:
        str_num = chr(temp % inp_B - 10 + ord('A'))
        lst_output.insert(0, str_num)
    temp = temp // inp_B

# output : B진법 수 (계산시 append 를 사용했으므로 reverse해서 출력)
output = ''.join(lst_output)
print(str(output))

# 알게된 점
# 1. string 형태로 insert 해야 ['1', 'a', '2'] 이런식으로 list에 추가됨.
# 12줄의 str을 빼게 되면 [1, 'a', 2] 이런식으로 list에 추가되어 join 연산 때 typeError 발생