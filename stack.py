class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        # instead of if self.list == []
        if not self.list:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element was inserted"

    def pop(self):
        if self.is_empty():
            return "No elements in stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "There are no elements in stack"
        else:
            #either or
           # return self.list[-1]
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.peek())
print(stk)
