class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def Min_value_Tree(root):
    if not root:
        return float('inf')
    return min(root.val,Min_value_Tree(root.left),Min_value_Tree(root.right))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Min_value_Tree(root))