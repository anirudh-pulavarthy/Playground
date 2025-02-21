# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def recurse(node, x):
            if not node: return

            self.vals.add(x)
            recurse(node.left, (2 * x) + 1)
            recurse(node.right, (2 * x) + 2)

        self.vals = set()
        recurse(root, 0)
        
    def find(self, target: int) -> bool:
        return target in self.vals
        
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)