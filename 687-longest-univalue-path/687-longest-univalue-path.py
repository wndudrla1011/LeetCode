# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return 0

            # search leaf nodes
            left = dfs(node.left)
            right = dfs(node.right)

            # calculate a distance
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # calculate a longest distance
            self.result = max(self.result, left+right)
            # maintain a status value(longest path)
            return max(left, right)

        dfs(root)
        return self.result