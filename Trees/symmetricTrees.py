class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def sameTrees(t1,t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val) and sameTrees(t1.left,t2.left) and sameTrees(t1.right,t2.right)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(54)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
print(sameTrees(root,root2))