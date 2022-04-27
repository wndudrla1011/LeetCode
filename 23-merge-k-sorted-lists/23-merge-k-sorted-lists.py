# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        data = []

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        # lst -> ListNode
        for lst in lists:
            if lst == None:
                continue
                
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