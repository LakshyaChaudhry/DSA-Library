# This file is for a backtracking implementation of a path sum problem

def hasPathSum(root, targetSum):
    if root == None:
        return False
        
    if root.left == None and root.right == None:
        return targetSum == root.val
        
    left = hasPathSum(root.left, targetSum - root.val)
    right = hasPathSum(root.right, targetSum - root.val)
    return left or right

