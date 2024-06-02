class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def maxpathsum(root):
    def dfs(root,path,maxsum):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            currsum = sum(path)
            maxsum = max(currsum,maxsum)
        else:
            if root.left:
                dfs(root.left,path,maxsum)
            if root.right:
                dfs(root.right,path,maxsum)
        path.pop()
    maxsum = 0
    dfs(root,[],maxsum)
    return maxsum
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(11)
print(maxpathsum(root))