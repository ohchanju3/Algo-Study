# 부등호 ( https://www.acmicpc.net/problem/2529 )
# input : 부등호의 개수와 부등호 문자열
K = int(input())
lst = list(map(str, input().split()))

# output : 부등호 관계를 만족하는 최댓값과 최솟값
def min_num(lst, K):
    num_lst = [i for i in range(10)]
    temp_num_lst = num_lst
    output = []
    count = 0
    for i in range(K):
        if lst[i] == '>':
            count = count + 1
            if i == K-1:
                for j in range(count, -1, -1):
                    output.append(temp_num_lst[j])
        else:
            for j in range(count, 0, -1):
                temp = temp_num_lst[j]
                temp_num_lst.remove(temp)
                output.append(temp)
            
            temp = temp_num_lst[0]
            temp_num_lst.remove(temp)
            output.append(temp)
            count = 0
            if i == K-1:
                output.append(temp_num_lst[0])
    
    return ''.join(map(str, output))

def max_num(lst, K):
    num_lst = [i for i in range(9, -1, -1)]
    temp_num_lst = num_lst
    output = []
    count = 0
    for i in range(K):
        if lst[i] == '<':
            count = count + 1
            if i == K-1:
                for j in range(count, -1, -1):
                    output.append(temp_num_lst[j])
        else:
            for j in range(count, 0, -1):
                temp = temp_num_lst[j]
                temp_num_lst.remove(temp)
                output.append(temp)
            
            temp = temp_num_lst[0]
            temp_num_lst.remove(temp)
            output.append(temp)
            count = 0
            if i == K-1:
                output.append(temp_num_lst[0])
    
    return ''.join(map(str, output))

print(max_num(lst,K))
print(min_num(lst,K))