# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # reverse
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # linked_list -> list
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list


    # list -> linked_list
    def toReverseLinkedList(self, result):
        prev = None

        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(resultStr))
