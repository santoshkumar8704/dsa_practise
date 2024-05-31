class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedStack:
    def __init__(self):
        self.Head = None
        self.count = 0
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.Head
        self.Head = new_node
        self.count += 1
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        res = self.Head
        self.Head = self.Head.next
        self.count -= 1
        return res.val
    def peak(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.Head.val
    def isEmpty(self):
        return self.Head is None
    def length(self):
        return self.count
linked_list_stack = LinkedStack()

linked_list_stack.push(1)
linked_list_stack.push(2)
linked_list_stack.push(3)

print(linked_list_stack.peak())  # Output: 3
print(linked_list_stack.pop())   # Output: 3
print(linked_list_stack.isEmpty())  # Output: False
print(linked_list_stack.pop())   # Output: 2
print(linked_list_stack.pop())   # Output: 1
print(linked_list_stack.isEmpty())  # Output: True
