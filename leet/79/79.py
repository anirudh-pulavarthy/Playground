from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # This set contains a set of all the positions in the board that are visited
        # Using this to find out if I visited a position or not in O(1) time
        visited = set()

        # Define a dfs function that tried to find character at position 'i'
        # at board position 'r' & 'c'
        # If the character is not found, return False
        def dfs(r, c, index):

            # Reached the end of string? Hurray!!
            if index == len(word):  return True

            elif (r < 0 or c < 0 or r >= m or c >= n ## Out of board's bounds
                or (r, c) in visited    # cannot visit a position that is already visited
                or board[r][c] != word[index]):  # if the position (r,c) in the board does not have the character we are looking for
                    
                return False

            # Add this position to the set, so that the further calls to dfs
            # in the current path know this position is already visited.            
            visited.add((r, c))

            # For the character at 'index + 1', visit all four directions to find out
            res = ((dfs(r, c + 1, index + 1)) or    # Visit right
                (dfs(r, c - 1, index + 1)) or  # visit left
                (dfs(r - 1, c, index + 1)) or # visit top
                (dfs(r + 1, c, index + 1))) # visit bottom
            
            # Once we traverse all paths in the current scenario, remove the pos
            visited.remove((r, c))

            return res

        # Now that we defined a dfs function to traverse the board,            
        # we must visit every position in the board to find the "word"
        for i in range(m):
            for j in range(n):
                # Iterate starting at (i, j) and index 0 at word
                # First instance when the dfs function returns true, is when we found the word!
                if dfs(i, j, 0): return True

        # Otherwise, the word isn't present in the board :')
        return False

