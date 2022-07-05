class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        other = [0] * len(nums)
        
        for i in range(len(nums)):
            new_pos = i + k
            if new_pos >= len(nums): 
                new_pos = new_pos % len(nums)
            other[new_pos] = nums[i]
        
        
        for i in range(len(other)): 
            nums[i] = other[i]
        