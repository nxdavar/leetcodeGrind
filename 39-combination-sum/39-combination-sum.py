class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort list
        candidates.sort()
        result = []
        curr_list = []
        curr_sum = target
        
        def helper(curr_sum, curr_list, candidates, result, start):
            if curr_sum < 0: 
                return
            
            elif curr_sum == 0:                
                result.append(list(curr_list))
                return
            
            for i in range(start, len(candidates)):
                curr_list.append(candidates[i])
                helper(curr_sum - candidates[i], curr_list, candidates, result, i)
                del curr_list[-1]
                
        helper(curr_sum, curr_list, candidates, result, 0)
            
        return result
                
            
            