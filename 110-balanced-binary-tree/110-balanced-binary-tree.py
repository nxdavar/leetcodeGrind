# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # empty case return true
        if not root: 
            return True
        
        #call the self.helper function here
        return self.helper(root) != -2
    
    def helper(self, node): 
        if node is None: 
            return -1
        
        left_sum =  1
        right_sum = 1
        
        left_add = self.helper(node.left)
        if left_add == -2: 
            return -2
        
        right_add = self.helper(node.right)
        if right_add == -2: 
            return -2
        
        left_sum += left_add
        right_sum += right_add
        
        if abs(left_sum - right_sum) > 1: 
            return -2
        
        return max(left_sum, right_sum)
        