# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        in_order = []
        q = deque()
        
        if root is None:
            return []
        
        curr_level = 0
        curr_list = []
        q.append(root)
        q.append(0)
           
        while len(q) > 0: 
            temp_node = q.popleft()
            temp_lvl = q.popleft()
            
            if curr_level != temp_lvl:
                in_order.append(curr_list)
                curr_list = []
                curr_level = temp_lvl
            
            curr_list.append(temp_node.val)
            
            
            if temp_node.left is not None: 
                q.append(temp_node.left)
                q.append(temp_lvl + 1)
                
            if temp_node.right is not None: 
                q.append(temp_node.right)
                q.append(temp_lvl + 1)
        
        in_order.append(curr_list)
    
        return in_order
                
        