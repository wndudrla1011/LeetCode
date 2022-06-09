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
        if root:
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
            if root.val >= low and root.val <= high:
                self.result += root.val

        return self.result