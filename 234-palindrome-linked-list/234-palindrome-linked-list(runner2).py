import sys


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

curr_node.next = ListNode(2)
curr_node = curr_node.next

curr_node.next = ListNode(1)
curr_node = curr_node.next


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
        print(False)
        sys.exit(0)
    slow, rev = slow.next, rev.next

print(True)
