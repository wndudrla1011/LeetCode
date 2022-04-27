import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    data = []

    if len(lists) == 0:
        return None

    if len(lists) == 1:
        return lists[0]

    # lst -> ListNode
    for lst in lists:
        if lst.__len__() == 0:
            continue

        # if lst == None:
        #     continue

        data.append(lst.val)
        # input lists[i+1:]
        while lst.next:
            lst = lst.next
            data.append(lst.val)

    lists = ListNode()
    # case: inputed data is configured of []
    if len(data) == 0:
        return None
    data.sort()

    for i in range(len(data)):
        if i == 0:
            lists.val = data[i]
        else:
            # store lists
            node = lists
            # if node.next is None, move a node's pointer to last position
            while node.next:
                node = node.next
            # add next data from the last position
            node.next = ListNode(data[i])

    return lists


head1, head2, head3 = ListNode(1), ListNode(1), ListNode(2)

curr_node1, curr_node2, curr_node3 = head1, head2, head3

curr_node1.next, curr_node2.next, curr_node3.next = ListNode(4), ListNode(3), ListNode(6),
curr_node1, curr_node2, curr_node3 = curr_node1.next, curr_node2.next, curr_node3.next

curr_node1.next, curr_node2.next = ListNode(5), ListNode(4)
curr_node1, curr_node2 = curr_node1.next, curr_node2.next

lists = [head1, head2, head3]

result = mergeKLists([[],[]])

print(result)