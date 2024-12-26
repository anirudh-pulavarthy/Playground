from typing import Optional

# Leetcode problem 543: Finding the diameter of a binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def recursivefunc(node: Optional[TreeNode]) -> int :
            if node is None: return 0
            lheight = recursivefunc(node.left)
            rheight = recursivefunc(node.right)
            
            nonlocal result
            if (lheight + rheight > result): result = lheight + rheight
            return 1 + max(lheight, rheight)
        
        if root:
            recursivefunc(root)
            return result
        else:
            return 0

if __name__ == "__main__":
    node = [1,2]

    s = Solution()
    res = s.diameterOfBinaryTree(node)
    print("Solution = ", res)
