# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif (p and not q) or (q and not p): return False

        if p.val != q.val: return False

        if p.left and not q.left: return False
        if q.left and not p.left: return False

        if not self.isSameTree(p.left, q.left): return False

        if p.right and not q.right: return False
        if q.right and not p.right: return False

        if not self.isSameTree(p.right, q.right): return False
        return True
