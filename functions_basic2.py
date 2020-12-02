# 1
def a(num): 
    countdown = []
    for x in range(num, -1, -1):
        countdown.append(x)
    return countdown

print(a(6))

# 2
def b(list):
    print(list[0])
    return list[1]
b([1,2])
    
# 3
def c(list):
    return (list[0] + len(list))
print(c([1,2,3,4,5,6,7]))

# 4
def d(list):
    new_list = []
    values = 0
    for i in range(len(list)):
        if list[i] > list[1]:
            values += 1
            new_list.append(list[i])
    return new_list
    print(values)
print(d([1,2,3,4,5,6]))

# 5
def e(size, value):
    e_list = []
    for i in range(size):
        e_list.append(value)
    return e_list
print(e(3,6))