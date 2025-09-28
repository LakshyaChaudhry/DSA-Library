#this code is to implement DFS traversal of a matric

def matrixDFS(matrix, r, c, visit):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] == 1 or visit[r][c]:
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    visit.add((r, c))
    
    count = 0
    count += matrixDFS(matrix, r + 1, c, visit)  # down
    count += matrixDFS(matrix, r - 1, c, visit)  # up
    count += matrixDFS(matrix, r, c + 1, visit)  # right
    count += matrixDFS(matrix, r, c - 1, visit)  # left

    visit.remove((r, c))
    return count