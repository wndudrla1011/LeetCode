# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []

        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            result = min(result, node.val - prev)
            prev = node.val
            
            node = node.right
            
        return result