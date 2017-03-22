

def eq_index(a):
    hasmap ={}
    sum = 0
    for i in range(0, len(a)):
        hasmap[i] = sum
        sum = sum + a[i]

    print hasmap

    sum2 = 0
    for i in range(len(a)-1, -1, -1):
        # print i
        # print a[i]
        if sum2 == hasmap[i]:
            return i
        else:
            sum2 = sum2 + a[i]

    return -1


print eq_index([-1, 3, -4, 5, 1, -6, 2, 1])
print eq_index([-100, 0, -100])
print eq_index([5, 5, 5, 5,6, 5, 5, 5,5])
