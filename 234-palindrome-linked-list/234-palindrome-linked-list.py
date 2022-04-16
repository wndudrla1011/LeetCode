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
        slow = fast = head
        rev = None

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            next, head.next = head.next, rev
            rev, head = head, next

        if fast:
            slow = slow.next

        while slow:
            if rev.val != slow.val:
                return False
            slow, rev = slow.next, rev.next

        return True