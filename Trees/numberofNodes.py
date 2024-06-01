class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def countNodes(root):
    if not root:
        return 0
    return countNodes(root.left)+countNodes(root.right)+1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(11)
print(countNodes(root))