# we need a node class because the list is made up of nodes
# each node has a value and also knows where the next node is


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# need a class to represent the linkedlist
# has to have a head and a tail


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        if self.head is None:
            print('The singly linked list doesn\'t exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, value):
        index = 0
        if self.head is None:
            return 'list empty value doesn\'t exist'
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    print(f"{value} found")
                    return node
                node = node.next
            return 'Value not found'

    def delete_node(self, location):
        if self.head is None:
            print('The SLL does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def delete_all(self):
        if self.head is None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(0, 3)
print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(8))
singlyLinkedList.delete_node(4)
print([node.value for node in singlyLinkedList])
