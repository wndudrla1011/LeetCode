# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        
        def dfs(node):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            next_left, next_right = node.left, node.right
            
            node.left = next_right
            node.right = next_left

            return max(left, right) + 1

        dfs(root)

        return root