class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        if target < nums[0]:
            return 0
        
        
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        
        while l < r: 
            mid = (l + r) // 2
            if nums[mid] < target: 
                l = mid + 1
            elif nums[mid] > target: 
                r = mid
            else: 
                return mid
            
        return l
       
            
    
    