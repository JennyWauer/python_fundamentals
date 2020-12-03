numbers = [4,1,6,2,51,8,14,9]

# takes list, compares index with next index, moves index if index +1 is lower, return list
def num_sort(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
    return list

print(num_sort(numbers))