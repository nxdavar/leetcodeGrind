class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # understand: 
        # [1, 2, 9, 10]
        # [1,2]
        if len(nums) <= 1: 
            return 0
        
        nums.sort()
        middle = nums[len(nums) // 2]
        sum = 0
        for i in range(len(nums)): 
            if nums[i] != middle: 
                sum += (abs(middle - nums[i]))
                
        return sum
            