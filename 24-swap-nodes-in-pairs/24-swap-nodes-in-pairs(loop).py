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

root = prev = ListNode(None)
prev.next = head

while head and head.next:
    b = head.next
    head.next = b.next
    b.next = head

    prev.next = b

    head = head.next
    prev = prev.next.next

print(root.next)
