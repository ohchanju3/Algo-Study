A, B, V = map(int, input().split())
result = (V-B)/(A-B)

if result == int(result):
    print(int(result))
else:
    print(int(result) + 1)