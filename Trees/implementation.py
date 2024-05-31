class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.insert_recursively(self.root,val)
    def insert_recursively(self,node,value):
        if node.val > value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self.insert_recursively(node.left,value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self.insert_recursively(node.right,value)
    def delete(self,value):
        if not self.root:
            return None
        self.delete_recursively(self.root,value)
    def delete_recursively(self,node,value):
        if node.val == value:
            if node.left:
                
        elif node.val > value:
            self.delete_recursively(self,node.left,value)
        else:
            self.delete_recursively(self,node.right,value)


    def inorder(self):
        result = []
        self.inorder_recursive(self.root,result)
        return result
    def inorder_recursive(self,node,result):
        if node:
            self.inorder_recursive(node.left,result)
            result.append(node.val)
            self.inorder_recursive(node.right,result)
t = Tree()
t.insert(5)
t.insert(3)
t.insert(6)
t.insert(2)
t.insert(7)
print(t.inorder())
