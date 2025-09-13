#this file is for insertion of a node into a BST

class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(root, val):
    if root == None:
        return treeNode(val)
    if val < root.val:
        if root.left == None:
            root.left = treeNode(val)
        else:
            root.left = insertNode(root.left, val)
    else:
        if root.right == None:
            root.right = treeNode(val)
        else:
            root.right = insertNode(root.right, val)
    return root

