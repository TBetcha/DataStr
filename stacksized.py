class Stack:

    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element was added"

    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            return self.list[len(self.list) - 1]

    def del_stack(self):
        self.list = None


stk = Stack(4)
print(stk.is_empty())
print(stk.is_full())
stk.push(1)
stk.push(2)
stk.push(3)
print(stk)
