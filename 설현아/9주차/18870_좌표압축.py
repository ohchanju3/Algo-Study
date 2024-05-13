N = int(input())
lst = list(map(int, input().split()))

sorted_lst = sorted(list(set(lst)))
dic = {sorted_lst[i] : i for i in range(len(sorted_lst))}
for i in lst:
    print(dic[i], end = ' ')