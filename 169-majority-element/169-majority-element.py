class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # understand: 
        # [2,2,1,1,2,2]
        freq_tracker = {}
        for i in range(len(nums)): 
            if nums[i] in freq_tracker: 
                freq_tracker[nums[i]] += 1
            else: 
                freq_tracker[nums[i]] = 1
            
            if freq_tracker[nums[i]] > len(nums) // 2: 
                return nums[i]
            
        return -1