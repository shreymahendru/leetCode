class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        walker = self
        a = ""
        while walker:
            a = a + str(walker.val) + '->'
            walker = walker.next
        return a.strip('->')

def common_elements(string, lst, ll):
    dic = {}
    for i in string:
        dic[i] = 1
    #had to put numbers instead of incresing it
    for i in lst:
        if i in dic.keys():
            dic[i] = 2

    while ll != None:
        print ll.val
        if ll.val in dic.keys() and dic[ll.val] == 2:
            dic[ll.val] = 3
        ll = ll.next
    answer =[]
    for element in dic.keys():
        if dic[element] == 3:
            answer.append(element)
    return answer

s = 'aabcckede'
l = ['a', 'd', 'f', 'k', 'l', 'm', 'e', 'e','k', 'c']
ll = ListNode('g')
ll.next =  ListNode('g')
ll.next.next =  ListNode('d')
ll.next.next.next =  ListNode('e')
ll.next.next.next.next =  ListNode('k')
print s
print l
print ll
print common_elements(s, l, ll)
