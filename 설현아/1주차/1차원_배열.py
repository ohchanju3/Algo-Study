# 10807_백준 배열
# n = int(input())
# x = list(map(int,input().split()))
# v = int(input())
# print(x.count(v))

# 10871_백준 배열
# n, x = map(int,input().split())
# a = list(map(int,input().split()))
# result = ""
# # print(list(filter(lambda i : i < x, a)))
# for i in a :
#   if i < x :
#     result = result + str(i) + " "
# print(result)

# 10818_백준 배열
# n = int(input())
# x = list(map(int, input().split()))
# # print(min(x), max(x))
# min = x[0]
# max = x[0]

# for i in range(1, n) :
#   if x[i] > max :
#     max = x[i]
#   if x[i] < min :
#     min = x[i]
# print(min, max)

# 2562_백준 배열
# max = 0
# n = 0

# for i in range(1, 10) :
#   new = int(input())
#   if new > max :
#     max = new
#     n = i

# print(max)
# print(n)

# 10810_백준 배열
# size, times = map(int, input().split())
# num_list = [0 for i in range(size)]

# for i in range(times) :
#   start, end, num = map(int, input().split())
#   for j in range(start-1, end) :
#     num_list[j] = num

# result = ""
# for i in num_list:
#   result += str(i) + " "
# print(result)

# 10813_백준 배열
# size, times = map(int, input().split())
# num_list = [i for i in range(1, size+1)]
# temp = 0

# for i in range(times):
#   a, b = map(int,input().split())
#   temp = num_list[a-1]
#   num_list[a-1] = num_list[b-1]
#   num_list[b-1] = temp

# result = ""
# for i in num_list:
#   result += str(i) + " "
# print(result)

# size, times = map(int, input().split())
# num_list = [i for i in range(1, size+1)]

# for i in range(times):
#   a, b = map(int,input().split())
#   num_list[a-1], num_list[b-1] = num_list[b-1], num_list[a-1]

# result = ""
# for i in num_list:
#   result += str(i) + " "
# print(result)

# 5597_백준 배열
# students = [i for i in range(1, 31)]
# for i in range(28):
#   students.remove(int(input()))

# for i in students :
#   print(i)

# 3052_백준 배열
# num_list = []
# for i in range(10):
#   a = int(input())
#   b = a % 42
#   if b not in num_list:
#     num_list.append(b)
# print(len(num_list))

# n = []
# for _ in range(10):
#   a=int(input())
#   b=a%42
#   n.append(b)
# s=set(n)
# print(len(s))

# 10811_백준 배열
# size, times = map(int, input().split())
# num_list = [i for i in range(1, size+1)]

# for i in range(times):
#   a, b = map(int, input().split())
#   x = num_list[a-1:b]
#   x.reverse()
#   num_list[a-1:b] = x

# for i in num_list:
#   print(i, end=" ")

# 1546_백준 배열
n = int(input())
scores = list(map(int,input().split()))
sum = 0
max = max(scores)

for score in scores:
  sum += (score/max*100)

print(sum/n)