def max_product_triplet(l):
    print l
    l.sort()
    prod = 1
    print l
    if l[0] < 0 and l[1] < 0:
        prod = l[0] * l [1] * l[2]
    if l[len(l) -1] > 0:
        prod = prod* l[len(l) -1]
    if l[len(l)-1] * l[len(l)-2] * l[len(l)-3] > prod:
        return l[len(l)-1] * l[len(l)-2] * l[len(l)-3]
    else:
        return prod


print max_product_triplet([-3, 1, 2, -2, 5, 6])
