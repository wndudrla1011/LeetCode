# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    balanced = False
    alert = True
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
            
        def dfs(t):
            if t is None:
                return -1

            left = dfs(t.left)
            right = dfs(t.right)

            self.balanced = (abs(left-right) <= 1)
            if not self.balanced:
                self.alert = False
            return max(left, right) + 1

        dfs(root)

        return self.balanced and self.alert