class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if not root:
        return -1
    if root.val == val:
        return root
    elif root.val > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


