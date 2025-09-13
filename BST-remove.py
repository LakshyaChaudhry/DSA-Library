#this file is for rewmoving a node from a BST

class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minValue(node):
    while node.left != None:
        node = node.left
    
    min_value = node
    return min_value

def removeNode(root, val):
    if root == None:
        return -1
    if val < root.val:
        root.left = removeNode(root.left, val)
    elif val > root.val:
        root.right = removeNode(root.right, val)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            min_node = minValue(root.right)
            root.val = min_node.val
            root.right = removeNode(root.right, min_node.val)
    return root