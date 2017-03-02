

def powerSet(set, new = []):
    print set
    print new
    if set == []:
        return [new]

    # if string[0] not in res:
    #     res.append(string[0])
    res = []
    with_i =  powerSet(set[1:], new + [set[0]])
    without_i = powerSet(set[1:], new)
    res.extend(with_i)
    res.extend(without_i)
    return res


print powerSet([1, 2, 3])

def strCombination(string, new = ''):
    print "string"
    print string
    print 'new'
    print new
    if string == '':
        return new.strip()
    res = ''
    with_i = strCombination(string[1:], new + string[0])
    without_i = strCombination(string[1:],new )
    print without_i
    print with_i
    if with_i != '':
        res = res + ' ' + with_i.strip()
    if without_i != '':
        res = res + ' ' + without_i.strip()
    return  res

print strCombination('123')

def maxsum(l, sum = 0):
    print l
    if l == []:
        return sum
    else:
        with_i = maxsum(l[2:], sum+l[0])
        without_i = maxsum(l[1:], sum)
        return max(with_i, without_i)

print maxsum([100,100, 3, 100])
