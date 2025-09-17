#this file is to compute the height of a binary tree

def height(root):
    if root == None:
        return -1
    
    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1
