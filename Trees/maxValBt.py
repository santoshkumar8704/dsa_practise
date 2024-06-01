class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def Max_value_tree(root):
    if not root:
        return float('-inf')
    return max(root.val,Max_value_tree(root.left),Max_value_tree(root.right))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(54)
print(Max_value_tree(root))