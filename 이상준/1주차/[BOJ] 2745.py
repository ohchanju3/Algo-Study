# 진법 변환 ( https://www.acmicpc.net/problem/2745 )
# input N, B 받아오기
inp_N, inp_B = map(str, input().split())
inp_B = int(inp_B)

# B진법수 N을 10진법으로 바꾸기 (항상 <= 1,000,000,000)
lst_inp_N = list(inp_N)
output = 0
for chr in lst_inp_N:
    if(ord(chr) >= ord('A')):
        output = output * inp_B + (ord(chr) - ord('A') + 10)
    else:
        output = output * inp_B + (int(chr) - 0)

print(output)

# 알게된 점
# 1. typeError는 연산에 불가능한 자료형을 넣으면 뜨는 오류이다.
# if문을 쓸 경우 test case를 나눠서 테스트하는 연습을 해보자.
# 2. ord는 아스키코드를 반환한다. 
# 3. 진법변환에 대한 추가공부가 필요하다.