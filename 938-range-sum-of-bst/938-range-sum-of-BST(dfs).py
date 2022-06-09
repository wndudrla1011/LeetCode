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
    result = 0
    def rangeSumBST(self, root, low, high):
        def dfs(root):
            if not root:
                return 0

            if root.val < low:
                return self.rangeSumBST(root.right, low, high)
            if root.val > high:
                return self.rangeSumBST(root.left, low, high)
            # <before previous code>
            # if low <= root.val <= high:
            #     self.result += root.val
            #     self.rangeSumBST(root.left, low, high)
            #     self.rangeSumBST(root.right, low, high)

            return root.val + \
                   self.rangeSumBST(root.left, low, high) + \
                   self.rangeSumBST(root.right, low, high)

        # return self.result
        return dfs(root)

s = Solution()
print(s.rangeSumBST(root, low, high))