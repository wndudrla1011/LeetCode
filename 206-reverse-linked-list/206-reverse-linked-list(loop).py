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

curr_node.next = ListNode(5)
curr_node = curr_node.next

node, prev = head, None

while node:
    next, node.next = node.next, prev
    prev, node = node, next

print(prev)