# 1
# def print_basic():
#     for x in range(1,256):
#         print(x)
# print_basic()

# 2
# def print_sum():
#     sum = 0
#     for x in range(1, 256):
#         sum += 1
#     print(sum)
# print_sum()

# 3
# def find_max(list):
#     max = list[0]
#     for x in range(len(list)):
#         if list[x] > max:
#             max = list[x]
#     print(max)
# find_max([1,2,3,4,5,6,7])

# 4
# def odd():
#     odd_list = []
#     for x in range(1,256): 
#         if x % 2 != 0:
#             odd_list.append(x)
#     return odd_list
# print(odd())

# 5 
# def greater(list, y):
#     count = 0
#     for x in range(len(list)):
#         if list[x] > y:
#             count += 1
#     return count
# print(greater([1,2,31,45,2,61,17], 4))

# 6
# def min_max_avg(list):
#     min = list[0]
#     max = list[0]
#     sum = 0
#     for x in range(len(list)):
#         if list[x] < min:
#             min = list[x]
#         if list[x] > max:
#             max = list[x]
#         sum += list[x]
#     avg = sum/len(list)
#     return min, max, avg
# print(min_max_avg([1,3,2,12,16, -2, 13]))

# 7
# def swap_neg(list):
#     for x in range(len(list)):
#         if list[x] < 0:
#             list[x] = "Dojo"
#     print(list)
# swap_neg([-1,3,-9,2,3])

# 8
# def print_odd():
#     for x in range(1,256):
#         if x % 2 != 0:
#             print(x)
# print_odd()

# 9
# def iterate(list):
#     for x in range(len(list)):
#         print(list[x])
# iterate([1,2,3,4,5,5,2,6])

# 10
# def get_avg(list):
#     sum = 0
#     for x in range(len(list)):
#         sum += list[x]
#     avg = sum/len(list)
#     return avg
# print(get_avg([1,5,12,1,3,1,12]))

# 11
# def square(list):
#     for x in range(len(list)):
#         list[x] = list[x] * list[x]
#     return list
# print(square([2,3,12,1,5,6]))

# 12 
# def zero(list):
#     for x in range(len(list)):
#         if list[x] < 0:
#             list[x] = 0
#     return list
# print(zero([2,-1,-14,12]))

# 13
def shift(list):
    for x in range(len(list)-1):
        list[x] = list[x+1]
    list[len(list)-1] = 0
    return list

print(shift([1,2,3,1,2,2,5,6,12]))