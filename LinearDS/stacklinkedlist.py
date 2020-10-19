class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def is_empty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            node_val = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_val

    def peek(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            node_val = self.LinkedList.head.value
            return node_val

    # delete entire stack
    def delete(self):
        self.LinkedList.head = None


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
print(stk.is_empty())
print(stk)
print('--------')
stk.pop()
print(stk)
print('--------')
print(stk.peek())
stk.delete()
print(stk)
