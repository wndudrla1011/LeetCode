class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head, list1, list2 = ListNode(-1), ListNode(1), ListNode(1)
cursor = head

curr_node1, curr_node2 = list1, list2

curr_node1.next, curr_node2.next = ListNode(2), ListNode(3)
curr_node1, curr_node2 = curr_node1.next, curr_node2.next

curr_node1.next, curr_node2.next = ListNode(4), ListNode(4)
curr_node1, curr_node2 = curr_node1.next, curr_node2.next

while list1 != None and list2 != None:
    if list1.val <= list2.val:
        cursor.next = list1
        list1 = list1.next
    else:
        cursor.next = list2
        list2 = list2.next

    cursor = cursor.next

# Last Node
if list1 != None:
    cursor.next = list1
else:
    cursor.next = list2

head = head.next
while head:

    if not head.next:
        print(head.val)
        break

    print(head.val, end='->')
    head = head.next