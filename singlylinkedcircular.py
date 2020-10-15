class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def create_csll(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"


circ = CircleLinkList()
circ.create_csll(1)
print([node.value for node in circ])