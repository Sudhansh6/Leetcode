# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            if targetSum - root.val:
                return False
            return True 

        res = None
        if root.left:
            res = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            res = res or self.hasPathSum(root.right, targetSum - root.val)
        
        return res