# 분해합 ( https://www.acmicpc.net/problem/2231 )
# 자연수 N이 주어짐
N = int(input())

# N의 가장 작은 생성자 구하기
start = max(1, N-9*len(str(N)))
for i in range(start, N):
    temp_sum = i
    temp_i = i

    while temp_i > 0:
        temp_sum = temp_sum + (temp_i % 10)
        temp_i = temp_i // 10

    if temp_sum == N:
        print(i)
        break
else:
    print(0)

'''
알고리즘 설명
N의 가장 작은 생성자는 N - (N의 자리수 * 9) 보다 항상 크거나 같다.
왜냐하면, 각 자리수는 0~9까지의 수 중 하나이기 때문이다.
따라서 생성자를 찾는 범위를 N-(N의 자리수 * 9) 에서 N사이로 잡아서 
계산시간을 줄이려고 시도하였다.

특정 경우에는 음수부터 루프가 시작되는 경우가 있는데 이경우를 제외하고 싶다는
생각이 들었다.
역시나...제출시 오류가 발생하였다. temp_i 가 0보다 작아지면 분해합부분을 코드가 하지 않는다.

그래서 0보다 작으면 1부터 루프를 진행하도록 코드를 바꾸어 보았다.
'''