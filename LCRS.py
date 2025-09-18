#this file is to get the height and size of a left-child right sibling tree

def height(node):
    if node == None:
        return -1
    return max(1 + height(node.left), height(node.right))