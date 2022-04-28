class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap(object):

    # defulat value : ListNode()
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # index is hash value (index == bucket)
        index = key % self.size

        # case : not exists a node in index
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # case : exists a node in index -> Linked List
        p = self.table[index]
        while p:
            # case : duplicated key -> update a value
            if p.key == key:
                p.value = value
                return
            # protect from NoneError
            if p.next is None:
                break
            # move to next node
            p = p.next
        # if not duplicated key, link the node as new node
        p.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.size

        # case : not exists node in index
        if self.table[index].value is None:
            return -1

        # case : exists a node in index
        p = self.table[index]
        while p:
            # if exists the key that I was looking for
            if p.key == key:
                return p.value
            # if not exists the key that I'm gonna find -> find it on the next node
            p = p.next
        # it's not exists
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size
        # case : it's impossible remove a value not exists
        if self.table[index].value is None:
            return

        # case : if the key is exists in index
        p = self.table[index]

        # case : set to ListNode() if that node is only one in index
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # prev : previous node, p : current node
        prev = p
        while p:
            # case : found a key that I was looking for
            if p.key == key:
                # cut the current node's connection
                prev.next = p.next
                return
            # case : not found a key that I was looking for -> move to next node
            # previous -> current, current -> next
            prev, p = p, p.next