class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            return
        self.items.pop()
    def peak(self):
        if not self.items:
            return None
        return self.items[-1]
    def isEmpty(self):
        if not self.items:
            return True
        return False
    def size(self):
        return len(self.items)
    def printStack(self):
        print(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
print(stack.isEmpty())
stack.printStack()