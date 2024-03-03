M = int(input())
N = int(input())
list = []

for i in range(M, N+1) :
    if i == 1 :
        pass
    elif i == 2 :
        list.append(i)
    else:
        for j in range(2, i) :
            if i % j == 0 :
                break
            elif j == i - 1 :
                list.append(i)
if len(list) == 0 :
    print('-1')
else:
    print(sum(list))
    print(min(list))