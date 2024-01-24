# input
A = []
str_max_length = 0
for i in range(5):
    A.append(list(map(str, input())))
    if str_max_length <= len(A[i]):
        str_max_length = len(A[i])

list_youngseok = []
for i in range(str_max_length+1):
    for j in range(5):
        try:
            list_youngseok.append(A[j][i])
        except:
            pass

# output 
str_youngseok = ''.join(map(str, list_youngseok))
print(str_youngseok)