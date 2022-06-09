class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


low, high = 7, 15

root = TreeNode(10)

curr_node = root

curr_node.left = TreeNode(5)
curr_node.right = TreeNode(15)

curr_node.left.left = TreeNode(3)
curr_node.left.right = TreeNode(7)

curr_node.right.right = TreeNode(18)

class Solution(object):
    def rangeSumBST(self, root, low, high):
        stack, sum = [root], 0

        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum

s = Solution()
print(s.rangeSumBST(root, low, high))