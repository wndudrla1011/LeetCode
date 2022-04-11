class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)

curr_node = head

curr_node.next = ListNode(2)
curr_node = curr_node.next

curr_node.next = ListNode(2)
curr_node = curr_node.next

curr_node.next = ListNode(1)
curr_node = curr_node.next

rev = None
slow = fast = head

# create Reverse Linked List with Runner
while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
if fast:
    slow = slow.next

# make sure the palindrome is right
while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next

print(not rev)