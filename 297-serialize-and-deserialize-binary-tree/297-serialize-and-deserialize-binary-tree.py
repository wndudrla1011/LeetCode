# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        # zero index won't use it
        result = ['@']

        while queue:
            node = queue.popleft()

            if node:
                # BFS
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                # handle None
                result.append('@')

        # from list to string
        return '#'.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # handle exception
        if data == '@#@':
            return None
        
        # from string to list
        nodes = data.split('#')

        # pop root value (except from zero index)
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        # child node's start point
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] != '@':
                # connect left child
                node.left = TreeNode(int(nodes[index]))
                # BFS
                queue.append(node.left)
            # next node
            index += 1

            if nodes[index] != '@':
                # connect right child
                node.right = TreeNode(int(nodes[index]))
                # BFS
                queue.append(node.right)
            # next node
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))