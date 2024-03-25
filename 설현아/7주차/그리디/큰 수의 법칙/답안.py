import time

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

start_time = time.time() # 시간 복잡도 측정

combi = (nums[-1] * k) + nums[-2] # k+1번

quotient = m // (k+1)
remainder = m % (k+1)

result = (combi * quotient) + (nums[-1] * remainder)

end_time = time.time() # 시간 복잡도 측정

print(result)
print(end_time - start_time)

# 소요시간 : 1.4
# 오답노트 : 문제의 핵심을 관통하면, 복잡하게 for/while문을 중첩하지 않아도 구현할 수 있었다. 얼마나 문제를 잘 이해하고 있는지가 가장 중요한 것 같다. 손으로 코드를 작성하기 전에, 문제에 대하여 고민하는 시간을 더 가져야겠다.