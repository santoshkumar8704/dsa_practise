class tr:
    def _init_(self,value):
        self.value=value
        self.left=None
        self.right=None
    
def preordertraversal(root):
    if root is None:
        return
    print(root.value," ",end ='')
    preordertraversal(root.left)
    preordertraversal(root.right)

def inordertraversal(root):
    if root == None:
        return
    inordertraversal(root.left)
    print(root.value," ",end ='')
    inordertraversal(root.right)

def postordertraversal(root):
    if root is None:
        return
    postordertraversal(root.left)
    postordertraversal(root.right)
    print(root.value," ",end='')
def levelOrder(root):
    if root == None:
        return
    result = []
    Q = 

o1 = tr (10)
o2 = tr (20)
o3 = tr (30)
o4 = tr (40)
o5 = tr (50)

o3.left=o2
o2.left=o1
o3.right=o4
o4.right=o5

inordertraversal(o3)
preordertraversal(o3)
postordertraversal(o3)