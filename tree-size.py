#this file is to get the total size of a tree

def tree_size(root):
    if root == None:
        return 0
    
    ls = tree_size(root.left)
    rs = tree_size(root.right)
    return (ls + rs + 1)
