class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def SymmetricTree(root):
    def is_mirror(t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and is_mirror(t1.left,t2.right) and is_mirror(t1.right,t2.left)
    return is_mirror(root,root)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(9)
root.left.left = TreeNode(4)
root.right.right = TreeNode(4)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# root.right.right.left = TreeNode(11)
print(SymmetricTree(root))