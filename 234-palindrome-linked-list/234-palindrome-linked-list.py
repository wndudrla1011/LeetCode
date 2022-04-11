# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = []

        if not head:
            return True

        node = head
        # transform to list
        while node is not None:
            # print(node.val)
            q.append(node.val)
            node = node.next

        # determine whether it is a palindrome or not
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True