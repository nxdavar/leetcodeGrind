class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        
        index = 0
        result = []
        
        while index < len(nums): 
            l = index + 1
            r = len(nums) - 1
            while l < r: 
                curr = nums[l] + nums[r] + nums[index]
                if curr > 0: 
                    r -= 1
                
                elif curr < 0: 
                    l += 1
                
                else: 
                    curr = []
                    curr.append(nums[l])
                    curr.append(nums[r])
                    curr.append(nums[index])
                    result.append(curr)
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                
            index += 1
            while index < len(nums) and nums[index] == nums[index - 1]: 
                index += 1
            
        return result