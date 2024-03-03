# 단어수학 ( https://www.acmicpc.net/problem/1339 )
# input : N과 N개의 단어
N = int(input())
lst = [str(input()) for i in range(N)]

def max_output(lst):
    max_num = 0
    dic = {}
    # 각 알파벳의 자리수 합 더해서 dictionary로 만들기
    for str in lst:
        for i,E in enumerate(str):
            if E not in dic.keys():
                dic[E] = 10**(len(str)-(i+1))
            else:
                dic[E] = dic.get(E) + 10**(len(str)-(i+1))
    
    # 가장 갯수가 많은 알파벳부터 정렬
    sorted_lst = sorted(dic.items(), reverse=True, key=lambda x:x[1])

    # 가장 갯수가 많은 알파벳부터 그 갯수와 9부터 0을 순서대로 곱해서 더함
    for i, value in enumerate(sorted_lst):
        max_num = max_num + (9-i)*value[1]
    
    return max_num

print(max_output(lst))


# GPT의 조언 (코드 리팩터링 관점)
'''
1. 변수 이름 사용: Python에서 str은 내장 함수 str()의 이름입니다. 
변수 이름으로 str을 사용하는 것은 이 내장 함수를 가리기 때문에 좋지 않습니다. 
대신 word와 같은 의미 있는 이름을 사용하는 것이 더 나을 것입니다.

2. dic.get(E)의 불필요한 사용: 이미 알파벳 E가 dic에 존재하는지 확인한 후에 dic.get(E)를 호출하는 것은 불필요합니다. 
이 경우 dic[E]로 직접 접근하는 것이 더 효율적입니다.

3. 자리 수 계산의 효율성: 10**(len(str)-(i+1))는 각 알파벳의 가중치를 계산하는 데 사용됩니다. 
이는 정확하지만, enumerate 함수를 사용할 때 reversed 함수나 다른 방식으로 역순 인덱스를 계산하는 것이 더 직관적일 수 있습니다.

4. 코드 정리: 코드를 좀 더 간결하고 읽기 쉽게 만들 수 있습니다.
'''
# def max_output(words):
#     weight = {}
#     for word in words:
#         k = len(word) - 1  # 가중치를 계산하기 위한 지수
#         for char in word:
#             if char in weight:
#                 weight[char] += 10**k
#             else:
#                 weight[char] = 10**k
#             k -= 1  # 다음 문자에 대한 가중치 감소

#     # 가중치에 따라 내림차순으로 정렬하고, 가장 높은 가중치부터 9부터 0까지 값을 할당
#     sorted_weights = sorted(weight.values(), reverse=True)
#     max_num = sum(val * (9 - i) for i, val in enumerate(sorted_weights))
    
#     return max_num

# # 입력 받기
# N = int(input())
# lst = [input() for _ in range(N)]
# print(max_output(lst))