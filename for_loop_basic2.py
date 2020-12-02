# 1
def biggie(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie([1,-2,3,-4,5]))

# 2
def positives(list):
    positive_count = 0
    for i in range(len(list)):
        if list[i] > 0:
            positive_count += 1
    list[len(list) - 1] = positive_count
    return list
print(positives([1,-2,3,-4,5,6]))

# 3
def sum_totals(list):
    totals = 0
    for i in range(len(list)):
        totals += 1
    return totals
print(sum_totals([1,2,3,4,5]))

# 4
def avg(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    avg_totals = sum/len(list)
    return avg_totals
print(avg([12,2,34,4,5,16,7]))

# 5
def length(list):
    list_length = len(list)
    return list_length
print(length([1,2,3,4,5,6]))

# 6
def minimum(list):
    if list == []:
            return False
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min
print(minimum([1,2,3,4,5]))

# 7
def maximum(list):
    if list == []:
            return False
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max
print(maximum([1,2,3,4,5]))

# 8
def analysis(list):
    sum = list[0]
    min = list[0]
    max = list[0]
    for i in range(len(list)):
        sum += list[i]
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]
    avg = sum / len(list)
    return {
        "sumTotal": sum,
        "average": avg,
        "minimum": min,
        "maximum": max,
        "length": len(list)
    }
print(analysis([1,2,3,4,5,6,7,8]))

# 9
# create function takes list
    # return reverse function
    # do no create new list
def reverse(list):
    list_len = len(list)
    for i in range(int(len(list)/2)):
        temp = list[(len(list) - 1) - i]
        list[(len(list) - 1) - i] = list[i]
        list[i] = temp
    return list
print(reverse([1,2,3,4,5,6]))