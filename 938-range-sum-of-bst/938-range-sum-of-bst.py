# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(t):
            if t:
                dfs(t.left)
                dfs(t.right)
                if t.val >= low and t.val <= high:
                    self.result += t.val

            return t

        dfs(root)

        return self.result