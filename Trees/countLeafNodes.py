#Count the number of leaf nodes in a binary tree.
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def CountLeafNodes(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return CountLeafNodes(root.left)+CountLeafNodes(root.right)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(11)
print(CountLeafNodes(root))