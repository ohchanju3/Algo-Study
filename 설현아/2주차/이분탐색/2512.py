# 2512번: 예산

N = int(input())
requests = list(map(int,input().split()))
budget = int(input())

minprice = 0
maxprice = max(requests)

if sum(requests) <= budget :
  print(max(requests))
else :
  # 0 ~ max(requests)
  while minprice <= maxprice :
    mid = (minprice + maxprice) // 2
    total = 0

    for request in  requests :
      total += min(mid, request)

    if total <= budget : # 같을 경우에도 연산 필요함
      minprice = mid + 1
    else :
      maxprice = mid -1
  print(maxprice)