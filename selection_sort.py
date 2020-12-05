numbers = [4,1,6,2,51,8,14,9]

# takes list, compares index with next index, moves index if index +1 is lower, return list
def num_sort(list):
    for i in range(len(list)):
        min_num = i
        for x in range(i+1, len(list)):
            if list[x] < list[min_num]:
                min_num = x
        temp = list[i]
        list[i] = list[min_num]
        list[min_num] = temp
    return list
print(num_sort(numbers))