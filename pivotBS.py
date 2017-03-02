'''[3,8, 9, 10 , 11]

[10, 11, 3, 8, 9]

[10, 11, 14, 17, 18, 19, 3, 8, 9 ]

len = 5
l = 0
r = 8
m  = 4
while l < r:
    m = 4 , mid [m] = 18
    if  arr[l]< x < mid[m]

3 -> index 2


find index of min
offset = index of min '''

def find_pivot(lst, start, end):
    l = start
    r = end#8
    m = (r + l)/2 # 4
    print l
    print r
    print m
    # print lst
    if r - l == 1:
        return l
    if lst[r] < lst[m]:
        print lst[m:r]
        return find_pivot(lst, m, r)
    elif lst[l] > lst[m]:
        print lst[l:m]
        return find_pivot(lst, l, m)

lst = [10, 11, 14, 17, 18, 19, 3, 8, 9]
# print pivot( lst,0 , 8)
print "pivot"

def bSrearch(lst, element):
    print lst
    l = 0
    r = len(lst)
    while l <= r:
        print "left =" +str(l)
        print "right ="+str(r)
        m =  l + (r- l) /2
        m  = (l + r )/ 2
        print m
        # if lst[l] == element:
        #     retursn l
        # if lst[r] == element:
        #     return r
        if lst[m] == element:
            return m
        if element > lst[m]:
            l = m + 1
        if element < lst[m]:
            r = m - 1

# print bSrearch([1,2,3, 77, 99,5123,5124,12127, 232311,1111111], 5124)

def search(lst, element):
    pivot = find_pivot(lst, 0, len(lst)-1 )
    if lst[pivot] == element:
        return pivot
    if element > lst[0] and element < lst[pivot]:
        return bSrearch(lst[:pivot], element)
    if element >lst[pivot+1] and element < lst[len(lst) -1]:
        return pivot +1+ bSrearch(lst[pivot+1:] ,element)

print search([10, 11, 14, 17, 18, 19, 3, 8, 9], 8)
