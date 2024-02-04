# 약수들의 합 ( https://www.acmicpc.net/problem/9506 )

while 1:
    # input 받기
    inp = int(input())

    # input이 -1인경우 loop 종료
    if inp == -1:
        break
    
    # 약수 리스트 초기선언
    yaksu = []
    # 약수 받아오기
    for i in range(1, int(inp/2) + 1):
        if inp % i == 0:
            yaksu.append(i)
    
    # 결과 출력하기
    if sum(yaksu) != inp:
        print(f"{inp} is NOT perfect.")
    else:
        print(f"{inp} =", end = ' ')
        for i in yaksu:
            if i == yaksu[-1]:
                print(f"{i}")
            else:
                print(f"{i} +", end = ' ')

# 알게 된 점
# 1. 결과 출력코드가 좀 더러운데 join함수를 써보자