#Definition for singly-linked list.
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(0)
        carry = 0
        ret = answer
        while(l1 != None or l2 != None):
        	if l1:
        		a = l1.val
        	else:
        		a = 0
        	if l2:
        		b = l2.val
        	else:
        		b = 0
        	val = a + b + carry
        	carry = val/ 10
        	answer.next = ListNode(val % 10)
        	answer = answer.next
        	if (l1 != None):
        		l1 = l1.next
        	if (l2 != None):
        		l2 = l2.next

        if carry > 0:
        	answer.next = ListNode(carry)

       	return ret.next
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node != None or node.next != None:
            node.val = node.next.val
            node.next = node.next.next
            # print node.val
            # node = None
    def reveserLL(self, node):
        if node != None:
            ret = ListNode(node.val)
            while node.next != None:
                a = ListNode(node.next.val)
                a.next = ret
                ret = a
                node = node.next
            return ret

    def hasCycleMap(self, node):
        """
        :type head: ListNode
        :rtype: bool
        """
        map = []
        if node == None or node.next == None:
            return False
        while node.next != None:
            if node in map:
                return True
            else:
                map.append(node)
                node = node.next
        return False

    def hasCycleRunner(self, node):
        slow = node
        fast = node.next
        if fast.next == None:
            return False
        if fast.next.next == None:
            return False
        while fast.next != None  or fast.next.next != None:
            slow = slow.next
            fast =  fast.next.next
            if fast == slow:
                return True
        return False

    def merge2sortedLL(self, l1, l2):
        ret = ListNode(0)
        newlist = ret
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                ret.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                ret.next = ListNode(l2.val)
                l2 = l2.next
            # elif l1.val == l2.val:
            #     ret.next = ListNode(l1.val)
            #     l1 = l1.next
            #     l2 = l2.next
            ret = ret.next
        if l1 == None and l2 == None:
            return newlist.next
        if l1 == None and l2 != None:
            ret.next = l2
            return newlist.next
        if l1 != None and l2 == None:
            ret.next = l1
            return newlist.next


    def swapPairs(self, head ):
        print head
        l = head
        if not l:
            return None
        if not l.next:
            return l
        else:
            temp = l.next
            l.next = self.swapPairs(l.next.next)
            temp.next = l
            return temp






l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)
l1.next.next.next    = ListNode(400)
# l1.next.next.next  = l1.next
print l1

l2 = ListNode(1)
l2.next = ListNode(9)
l2.next.next = ListNode(10)
print l2
sol = Solution()
# print sol.merge2sortedLL(l1, l2)
print sol.swapPairs(l2)
# ans = sol.addTwoNumbers(l1, l2)
# print ans
# print sol.deleteNode(l2)
# print l2
# print sol.deleteNode(l1.next)
# print l1
# print sol.hasCycleRunner(l1)
# print sol.reveserLL(l1)
# print sol.reveserLL(l2)
