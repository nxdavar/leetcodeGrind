# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    # understand: 
    # match -> recursion, dfs
    # plan -> sum up left and right path => always return max of both 
    
        if root is None:
            return 0
    
        left = 0
        right = 0
    
        left += self.maxDepth(root.left)
        right += self.maxDepth(root.right)

        return 1 + max(left, right)