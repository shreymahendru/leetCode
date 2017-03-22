

def phone_number(a):
    a = a.replace(' ', '').replace('-', '')
    l = len(a)
    if l%3 == 0 or l%3 == 2:
        #can be divided into 3 eqaul blocks
        ret = ''
        cntr = 1
        for i in a:
            ret = ret + i
            if cntr%3 == 0 and cntr != len(a):
                ret = ret+ '-'
            cntr = cntr + 1
        return ret.strip('-')
    else:
        ret = ''
        cntr = 1
        for i in a:
            ret = ret+i
            print ret
            print len(a)- cntr
            if len(a)- cntr <=4:
                ret = ret+ '-'
                break

            if cntr%3 == 0:
                ret= ret+ '-'
                # break
            cntr = cntr+1
        print a[cntr:]
        c = 1
        for i in a[cntr:]:
            ret = ret +i
            if c%2 == 0 and c != len(a[cntr:]):
                ret = ret+'-'
            c = c+ 1
        return ret.strip('-')




print phone_number('123 123 - 123-111')
print phone_number('1q777-1')
