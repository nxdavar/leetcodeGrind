class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr_tank = 0
        total_tank = 0
        result_index = 0
        
        for i in range(len(gas)): 
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0: 
                result_index = i + 1
                curr_tank = 0
                
        return result_index if total_tank >= 0 else -1