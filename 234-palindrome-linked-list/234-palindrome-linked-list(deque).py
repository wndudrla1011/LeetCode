import collections
import sys


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

q = collections.deque()

if not head:
    print(True)

node = head
# 리스트 변환
while node is not None:
    # print(node.val)
    q.append(node.val)
    node = node.next

# 팰린드롬 판별
while len(q) > 1:
    if q.popleft() != q.pop():
        print(False)
        sys.exit(0)

print(True)
