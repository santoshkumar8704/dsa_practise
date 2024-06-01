
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
def levelPrinting(root,level):
    if not root:
        return []
    queue = [(root,1)]
    while queue:
        node,lvl = queue.pop(0)
        if lvl == level:
            print(node.val)
        elif lvl > level:
            break
        if node.left:
            queue.append((node.left,lvl+1))
        if node.right:
            queue.append((node.right,lvl+1))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)
print(levelPrinting(root,3))