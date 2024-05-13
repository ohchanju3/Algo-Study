city = int(input())
distance_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))
result, visit = 0, 0

while(True):
  gap = 1
  price = visit
  if visit > city-2:# 제일 왼쪽 도시에서 마지막 도시 직전까지
    break

  for i in range(visit+1, city-1): # 방문한 도시 이후의 주유소 가격 비교
    if price_list[visit]<price_list[i]:
      gap += 1
    else:
      break

  for _ in range(gap):
    result += distance_list[visit]*price_list[price]
    visit += 1

print(result)

# 결과가 옳긴 하지만, 코드가 너무 장황하고 반복문이 여러번 사용되어 성능 개선이 필요하다.