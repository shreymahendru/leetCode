


def count_duplicates(lst):
    dic = {}
    for i in lst:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    ans =0
    for j in dic.keys():
        if dic[j] >1:
            ans+=1

    return ans



print count_duplicates([1,3,1,4,5,6,3,2, 3,6])
