class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            values = [str(x) for x in self.items]
            return ' '.join(values)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def enq(self, value):
        self.items.append(value)
        return "The value was added"

    def deq(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            return self.items[0]


    def delete(self):
        self.items = None

qu = Queue()
print(qu.is_empty())
print(qu.enq(1))
print(qu.enq(2))
print(qu.enq(3))
print(qu.deq())
print(qu)
print(qu.peek())
qu.delete()
print(qu)