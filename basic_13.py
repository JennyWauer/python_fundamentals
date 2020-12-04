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
def greater(list, y):
    count = 0
    for x in range(len(list)):
        if list[x] > y:
            count += 1
    return count
print(greater([1,2,31,45,2,61,17], 4))