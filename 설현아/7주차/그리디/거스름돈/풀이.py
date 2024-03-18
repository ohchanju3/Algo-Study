import time


N = int(input())

start_time = time.time()

a = N // 500
b = (N % 500) // 100
c = (N % 100) // 50
d = (N % 50) // 10

end_time = time.time()

print(a, b, c, d)
print(end_time - start_time)

# 소요시간 : 9.1
# 오답노트 : 각 a, b, c, d 를 선언하고 괄호 안에 작성한 코드가 무의미하게 반복된다. 소요시간의 차이가 생각보다 많이 났다. for문을 활용하여 좀 더 정교화 해야한다.