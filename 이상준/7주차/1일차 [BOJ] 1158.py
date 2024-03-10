# 요세푸스 문제 ( https://www.acmicpc.net/problem/1158 )
# input : N, K
N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
output_lst = []
start_index = K-1

while arr:
    while start_index >= len(arr):
        start_index = start_index - len(arr)
    output_lst.append(str(arr.pop(start_index)))
    start_index = start_index - 1
    start_index = start_index + K

print('<', end='')
print(', '.join(output_lst), end='')
print('>')