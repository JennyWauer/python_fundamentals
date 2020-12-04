numbers = [4,1,6,2,51,8,14,9]

# takes list, compares index with next index, moves index if index +1 is lower, return list
def num_sort(list):
    min = list[0]
    for i in range(len(list)):
        if list[i]<min:
            min = list[i]
            
        print(min)
           
    return list

print(num_sort(numbers))