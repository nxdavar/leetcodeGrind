class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def markIsland(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0': 
                return
            
            grid[x][y] = '0'
            
            for i in range(len(xDir)):
                markIsland(x + xDir[i], y + yDir[i])
                    
            return
        
        num_islands = 0
        xDir = [-1, 1, 0, 0]
        yDir = [0, 0, 1, -1]
        for i in range(len(grid)): 
            row = grid[i]
            for j in range(len(row)): 
                if (grid[i][j] == '1'):
                    num_islands += 1
                    markIsland(i, j)
        
        return num_islands
        
        
                
                