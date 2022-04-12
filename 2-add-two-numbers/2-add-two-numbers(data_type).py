class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1, l2 = ListNode(2), ListNode(5)

curr_node1, curr_node2 = l1, l2

curr_node1.next, curr_node2.next = ListNode(4), ListNode(6)
curr_node1, curr_node2 = curr_node1.next, curr_node2.next

curr_node1.next, curr_node2.next = ListNode(3), ListNode(4)
curr_node1, curr_node2 = curr_node1.next, curr_node2.next


# reverse
def reverseList(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

# linked_list -> list
def toList(node):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    return list


# list -> linked_list
def toReverseLinkedList(result):
    prev = None

    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node


def addTwoNumbers(l1, l2):
    a = toList(reverseList(l1))
    b = toList(reverseList(l2))

    resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

    return toReverseLinkedList(str(resultStr))


result = addTwoNumbers(l1, l2)

while result:
    if result.next is None:
        print(result.val)
        break
    print(result.val, end='->')
    result = result.next
