#this is for bfs traversal / also level order traversal

from collections import deque

def bfs_traversal(root):
    if root == None:
        return None
    
    queue = deque()
    if root:
        queue.append(root)
    
    while len(queue) > 0:
        current = queue.popleft()
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)