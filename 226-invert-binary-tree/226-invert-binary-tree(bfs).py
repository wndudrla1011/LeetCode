import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        queue = collections.deque([root])
        # stack = collections.deque([root]) -> dfs

        while queue:
            # node = stack.pop() -> dfs
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
# tree = TreeNode(1, TreeNode(2))
s = Solution()
result = s.invertTree(tree)
print(result)