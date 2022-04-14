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


if head is None:
    print(None)

odd = head
even = head.next
even_head = head.next

while even and even.next:
    odd.next, even.next = odd.next.next, even.next.next
    odd, even = odd.next, even.next

odd.next = even_head
print(head)