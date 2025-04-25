n,x = map(int,input().split())
a= list(map(int,input().split()))

answer=[str(i) for i in a if i < x]

print(" ".join(answer))