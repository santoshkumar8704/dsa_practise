class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def heightOfTree(root):
    if not root:
        return 0
    left_height = heightOfTree(root.left)
    right_height = heightOfTree(root.right)
    return max(left_height,right_height)+1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(heightOfTree(root))