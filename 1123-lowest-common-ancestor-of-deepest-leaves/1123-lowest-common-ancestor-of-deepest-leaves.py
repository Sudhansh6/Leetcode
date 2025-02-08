# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dp = {}
        
        def depths(node):
            if not node:
                return 0

            if dp.get(node.val, None) is not None:
                return dp[node.val]
            
            dp[node.val] = 1 + max(depths(node.left), depths(node.right))
            return dp[node.val]

        depths(root)
        curr = root
        while True:
            if not curr.left and not curr.right:
                break
            if not curr.left:
                curr = curr.right
                continue
            if not curr.right:
                curr = curr.left
                continue
            if dp[curr.left.val] > dp[curr.right.val]:
                curr = curr.left
            elif dp[curr.left.val] < dp[curr.right.val]:
                curr = curr.right
            else:
                break
        return curr





            
