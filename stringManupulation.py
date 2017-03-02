def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0
        if needle == '':
            return -1
        if haystack == '':
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                str = haystack[i: i + len(needle)]
                if str == needle:
                    return i
            i += 1
        return -1
# print strStr('12346', '23')
# print strStr('aaaa', 'a')
# print strStr('', 'a')
# print strStr('a', '')
print strStr("mississippi", 'pi')



def myAtoi(string):
        """
        :type str: str
        :rtype: int
        """
        a = string.strip()
        if a =='':
            return 0
        sign = None
        if a[0] == '+':
            a = a[1:]
            sign = 1
        elif a[0] == '-':
            a = a[1:]
            sign = -1
        num = ''
        print a
        for i in a:
            print i
            try:
                num = num + str(int(i))
            except ValueError:
                break
        print num
        if num == '':
            return 0
        if sign:
            num = int(num) * sign

        num =int(num)
        if num > 2147483647:
            return 2147483647
        if num < -2147483647:
            return -2147483647
        else:
            return num


print myAtoi('     0100')
