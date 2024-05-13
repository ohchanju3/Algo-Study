N = int(input())
lst = []

for i in range(N):
    lst.append(input())

lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)