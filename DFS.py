#this file is for my DFS implementations
#DFS can be implemented 3 ways, in-order, pre-order and post-order
# in order: L -> Root -> R
# pre order: Root -> L -> R
# post order: R-> L -> root

def inorder_traversal(root):
    if root == None:
        return None
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)

def preorder_traversal(root):
    if root == None:
        return None
    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
    if root == None:
        return None
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val)