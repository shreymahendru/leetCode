def removeDuplicates(array):
    """
    :type nums1: String
    :rtype: int
    slow and fast runnner
    fucking stupid!!!!!!
    """
    i = 0
    if len(array) == 0:
        return 0

    for j in range(1, len(array)):
        if array[j] != array[i]:
            i +=1
            array[i] = array[j]
    return i + 1

print removeDuplicates([1,2,3,4,5])
# print removeDuplicates([1,1,3,2,4,3])
# print removeDuplicates([1,2,2,2,12])

def twoSum(array, target):
    """
    :type nums1: String
    :rtype: int
    dictionary sol
    """
    dic = {}
    for i in range(0,len(array)):
        if target - array[i] in dic.keys():
                return [dic[target - array[i]]+1, i+1]
        dic[array[i]] = i
print twoSum([1,2,4,5, 100], 101)
print twoSum([1,2,4,5,9], 7)

def twoSum2(array, target):
    """
    :type nums1: String
    :rtype: int
    2 pointers
    """
    start = 0
    end = len(array)-1
    while(start< end):
        sum = array[start] + array[end]
        if sum < target:
            start += 1
        elif sum > target:
            end -= 1
        else:
            return  [start+1 , end+1]
print twoSum2([1,2,4,5, 100], 101)
print twoSum2([1,2,4,5,9], 7)
