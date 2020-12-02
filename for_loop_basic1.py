for x in range(51):
    print(x)

for x in range(1001):
    x *= 5
    print(x)
    
for x in range(1, 1001):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

for x in range(500001):
    sum = 0
    if x % 2 != 0:
        sum = sum + x
print(sum)

for x in range(2018, -1, -4):
    print(x)

lowNum = 2
highNum = 15
mult = 3
for x in range(lowNum, highNum, mult):
    print(x)