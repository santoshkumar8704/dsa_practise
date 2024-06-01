class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def rootToLeaf(root):
    def dfs(root,path,allpaths):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            allpaths.append("->".join(path))
        else:
            if root.left:
                dfs(root.left,path,allpaths)
            if root.right:
                dfs(root.right,path,allpaths)
        path.pop()
    allpaths = []
    dfs(root,[],allpaths)
    return allpaths
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(11)
print(rootToLeaf(root))

