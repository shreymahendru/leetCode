class Solution(object):
    def is_hex(self, a):
            hex = 'abcbefABCDEF0123456789'
            for i in a:
                if i not in hex:
                    return False
            return True
    def validIPAddress(self, IP):
         #check IPv4
        if '.' in IP:
            split = IP.split('.')
            if len(split) != 4:
                return "Neither"
            for i in split:
                if i == '':
                    return "Neither"
                if i[0] == '0':
                    return "Neither"
                try:
                    if int(i) > 255:
                        return "Neither"
                except ValueError:
                        return "Neither"
            return 'IPv4'
    #check IPv6
        else:
            ary = IP.split(':')
            if len(ary) == 8:
                for i in xrange(len(ary)):
                    tmp = ary[i]
                    if len(tmp) == 0 or not len(tmp) <= 4 or not self.is_hex(tmp):
                        print arr[i]
                        return "Neither"
                    return "IPv6"
        return "Neither"



a = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
print Solution().validIPAddress(a)
