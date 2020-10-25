class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return "There are no elements in the queue"
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node

    def peek(self):
        if self.is_empty():
            return "There are no elements in the list"
        else:
            return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None


cust = Queue()
cust.enqueue(1)
cust.enqueue(2)
cust.enqueue(3)
print(cust)
print(cust.dequeue())
print(cust)
print(cust.peek())
