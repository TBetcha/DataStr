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
            node = node.next
            if node == self.tail.next:
                break

    def create_csll(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    def insert_csll(self, value, location):
        if self.head is None:
            return "the head ref is none"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
                #if i do it his way with this in I cant insert at index 1
            # elif location == 1:
            #     new_node.next = self.tail.next
            #     self.tail.next = new_node
            #     self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            return "The new node has been inserted"

    def traverse(self):
        if self.head is None:
            return "there  are no values in list"
        while self.head is not None:
            print(self.head.value)
            self.head = self.head.next
            if self.head == self.tail.next:
                break


circ = CircleLinkList()
circ.create_csll(1)
circ.insert_csll(0, 0)
circ.insert_csll(2, 0)
circ.insert_csll(3, 0)
circ.insert_csll(2, 0)
circ.insert_csll(6, 1)
circ.traverse()

print([node.value for node in circ])
