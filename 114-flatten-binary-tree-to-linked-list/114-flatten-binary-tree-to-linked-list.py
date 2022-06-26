# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        node_list = []
        if not root or (root.left is None and root.right is None):
            return
        
        def dfs_help(node, node_list): 
            if node is None: 
                return
            
            # append to list for now
            node_list.append(node)
            dfs_help(node.left, node_list) 
            dfs_help(node.right, node_list)
            
            return
        
        #call dfs function here: 
        dfs_help(root, node_list)
        
        #run through and make everyone's left node null
        for i, c in reversed(list(enumerate(node_list))):
            if i == len(node_list) - 1: 
                c.right = None
            
            else:
                c.right = node_list[i + 1]
            
            c.left = None
    
      
            
        
        