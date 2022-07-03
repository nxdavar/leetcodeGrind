class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        main = {0: 1}
        result = 0
        curr_sum = 0
              
        for i in range(len(nums)):
            curr_sum += nums[i]
            diff = curr_sum - k
            if diff in main: 
                result += main[diff]
            
            if curr_sum in main: 
                main[curr_sum] += 1
            
            else: 
                main[curr_sum] = 1
                
        
        return result
            