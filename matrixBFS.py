#implementation of BFS traversal of a matrix
from collections import deque
def matrixBFS(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        size = len(queue)
        for i in range(size):
            r, c = queue.popleft()
            if r == ROWS -1 and c == COLS -1:
                return length
            
            for dr, dc in directions:
                if min((r + dr), (c + dc)) < 0 or r + dr >= ROWS or c + dc >= COLS or matrix[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit:
                    continue
                visit.add((r + dr, c + dc))
                queue.append((r + dr, c + dc))
        length += 1
        

