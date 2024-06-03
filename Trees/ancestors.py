class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def ancestors (root,target):
    if not root:
        return False
    if root.val == target:
        return True
    if ancestors(root.left,target) or ancestors(root.right,target):
        print(root.val)
        return True
    return False
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(ancestors(root,root.left.right.val))