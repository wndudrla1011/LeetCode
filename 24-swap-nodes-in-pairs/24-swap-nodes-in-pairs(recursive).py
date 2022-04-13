class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)

curr_node = head

curr_node.next = ListNode(2)
curr_node = curr_node.next

curr_node.next = ListNode(3)
curr_node = curr_node.next

curr_node.next = ListNode(4)
curr_node = curr_node.next


def swapPairs(head):
    if head and head.next:
        p = head.next
        head.next = swapPairs(p.next)
        p.next = head
        return p

prev = swapPairs(head)





# while prev:
#     if prev.next is None:
#         print(prev.val)
#         break
#     print(prev.val, end='->')
#     prev = prev.next