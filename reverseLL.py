# Definition for singly-linked list.
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

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        l = head
        cntr= False
        while head.next != None and head.val != n:
            # print l
            if head.val == m:
                cntr = True
                ret = head
            if cntr:
                print ret
                # print head.val
                a = ListNode(head.next.val)
                a.next = ret
                ret = a
            head = head.next
        return head

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next    = ListNode(4)
l1.next.next.next.next    = ListNode(5)
print l1

print Solution().reverseBetween(l1, 2, 4)
