import time
'''
17 4
3
'''

n, k = map(int, input().split())
cnt = 0

start_time = time.time() # 시간 복잡도 측정

while True:
  target = (n//k)*k # target = 16 / 4 / 0
  cnt += n - target # cnt = 1 / - / 4
  n = target # n = 16 / 4 / 0

  if n < k:
    break
  cnt += 1 # cnt = 2 / 3
  n //= k # n = 4 / 1

cnt += (n - 1)

end_time = time.time() # 시간 복잡도 측정

print(cnt)
print(end_time - start_time)

# 소요시간 : 1.50
# 오답노트 : 책에서 제시한 답안이 더 효율적이라고 느껴진 부분은, 반복문을 돌면서 1씩 빼주는 것이 아니라는 점이다. 반복문의 횟수가 적어진다면 시간 복잡도가 훨씬 개선될 것이라는 것을 명심하고 있지만 이러한 해답을 고민하는 과정이 아직 어렵다. 더 많은 문제를 접해봐야겠다.
#          특히나 마지막 cnt += (n-1) 해당 코드를 잘 이해하지 못했는데, 직접 작성해보니 이해할 수 있었다. 수학적 사고를 길르는 데 초점을 맞춰야겠다.
