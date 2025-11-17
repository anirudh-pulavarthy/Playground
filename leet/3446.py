"""
Daily problem 28 Aug 2025

Learnings: 
Diagonal traversal of a matrix
    variants... 
    downwards, upwards
    in all four directions

Should learn spiral traversal later
"""

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        a1 = [2, 3, 4, 1, 0, 7]

        n = len(grid)
        f = lambda arr, rev = False: sorted(arr, reverse = rev)
        in_bounds = lambda i,j: (0 <= i < n) and (0 <= j < n)

        for k in range(1, n - 1):
            row, col = 0, k

            current = []
            while in_bounds(row, col):
                current.append(grid[row][col])
                row, col = row + 1, col + 1
            current.sort()

            row, col = 0, k
            while in_bounds(row, col):
                grid[row][col] = current.pop(0)
                row, col = row + 1, col + 1
        
        for k in range(n - 1, -1, -1):
            row, col = k, 0
            current = []
            while in_bounds(row, col):
                current.append(grid[row][col])
                row, col = row + 1, col + 1
            
            current.sort(reverse = True)
            row, col = k, 0
            while in_bounds(row, col):
                grid[row][col] = current.pop(0)
                row, col = row + 1, col + 1

        return grid