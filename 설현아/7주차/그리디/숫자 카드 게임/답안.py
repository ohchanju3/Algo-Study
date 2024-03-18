import time


n, m = map(int, input().split())
max_num = 0

start_time = time.time() # 시간 복잡도 측정

for i in range(n):
  row = list(map(int, input().split()))
  max_num = max(max_num, min(row))

end_time = time.time() # 시간 복잡도 측정

print(max_num)
print(end_time - start_time)

# 소요시간 : 0.33
# 오답노트 : 시간 복잡도는 나의 풀이와 모범 답안이 거의 유사하다. 그러나 나의 풀이는 2차원 배열인 table을 정의해줌으로, 공간 복잡도 측면에서 답안에 비해 효율성이 떨어진다고 판단하였다. 그리고 if문으로 max_num을 갱신해주었는데 그 대신, max문법으로 간단히 표기할 수 있음을 알게 되었다.