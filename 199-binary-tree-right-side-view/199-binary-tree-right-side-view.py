# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        main = collections.deque()
        main.append(root)
        result = []
        
        while len(main) > 0:
            curr_len = len(main)
            right_most = None
            index = 0
            
            for i in range(curr_len): 
                curr = main.popleft()
                if curr: 
                    right_most = curr
                    main.append(curr.left)
                    main.append(curr.right)
            
            if right_most: 
                result.append(right_most.val)
            
        return result
               
            
            