# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        
        
        # ex: 
        q = deque()
        q.append(root)
        
        levels = deque()
        levels.append(1)
        
        
        while len(q) > 0:
            curr_popped = q.popleft()
            curr_level = levels.popleft()
            if curr_popped.left or curr_popped.right: 
                if curr_popped.left: 
                    q.append(curr_popped.left)
                    levels.append(curr_level + 1)
                if curr_popped.right: 
                    q.append(curr_popped.right)
                    levels.append(curr_level + 1)
                
            else: 
                return curr_level
            
        
        