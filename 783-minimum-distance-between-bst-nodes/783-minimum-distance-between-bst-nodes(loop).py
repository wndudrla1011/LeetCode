import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)

curr_node = root

curr_node.left = TreeNode(2)
curr_node.right = TreeNode(6)

curr_node.left.left = TreeNode(1)
curr_node.left.right = TreeNode(3)

class Solution(object):
    def minDiffInBST(self, root):
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


s = Solution()
print(s.minDiffInBST(root))