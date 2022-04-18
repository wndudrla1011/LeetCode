# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, odd, even = head, ListNode(None), ListNode(None)
        odd_list, even_list = odd, even

        number, cnt = 1, 0
        while node:
            if number % 2 != 0:
                odd.next, next = node, node.next
                odd = odd.next
                cnt += 1
            else:
                even.next, next = node, node.next
                even = even.next
            node = next
            number += 1
        else:
            if number % 2 != 0:
                odd.next = node
            else:
                even.next = node

        result = odd_list.next
        while cnt:
            odd_list = odd_list.next
            cnt -= 1
            
        odd_list.next = even_list.next
        
        return result