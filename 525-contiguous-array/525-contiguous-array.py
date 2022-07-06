class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        main = {}
        curr_sum = 0
        result = 0
        
        for i in range(len(nums)): 
            best = 0
            if nums[i] == 0:
                curr_sum -= 1
            else: 
                curr_sum += 1
            
            if curr_sum == 0: 
                best = i + 1
            
            elif curr_sum in main:
                best = i - main[curr_sum]
                
            #record max        
            result = max(result, best)
            
            if curr_sum not in main: 
                main[curr_sum] = i
        
        return result
            