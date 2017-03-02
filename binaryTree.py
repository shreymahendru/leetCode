# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dept(root)

    def dept(self,root,  d=0):
        # print d
        if root == None:
            return 0
        else:

            dept_left = self.dept(root.left, d) + 1
            dept_right = self.dept(root.right, d) + 1
            return max(dept_right, dept_left)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) and p.val == q.val

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum = sum-root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def rootToLeaf(self, root , paths, path):
        # if not root:
        #     return paths
        if root.left == None and root.right == None:
            paths.append(path + str(root.val))
        else:
            if root.left:
                self.rootToLeaf(root.left, paths, path+ str(root.val)+'->')
            if root.right:
                self.rootToLeaf(root.right, paths, path+str(root.val)+ '->')

    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))

t = TreeNode(2)
t.left = TreeNode(1100)
t.right = TreeNode(3)
# t.left.left = TreeNode(11)
# t.left.left.left = TreeNode(11)
# t.right.right = TreeNode(5)
# t.right.right.right = TreeNode(5)
# t.right.right.right.right = TreeNode(5)

y = TreeNode(4)
y.left = TreeNode(5)
y.right = TreeNode(5)
y.left.left = TreeNode(11)
y.left.left.left = TreeNode(11)
y.right.right = TreeNode(5)
y.right.right.right = TreeNode(5)
y.right.right.right.right = TreeNode(123)

paths = []
path = ""
# print Solution().rootToLeaf(y, paths,path)
# print paths
print Solution().isValidBST(t)
# print Solution().maxDepth(t)
