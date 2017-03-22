




def braces(lst):
    a = []
    for i in lst:
        if isValid(i):
            a.append('YES')
        else:
            a.append('NO')

    return a



def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    opn = {'(':')', '[':']', '{':'}'}
    clse = [')', ']', '}']
    stack = []
    for i in s:
        if i in opn.keys():
            stack.append(i)
            continue
        if i in clse:
            if len(stack) != 0 and  i == opn[stack[len(stack)-1]]:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True


print isValid('{()}')
print isValid('{[}')


print braces(['{()}','{[}'])
