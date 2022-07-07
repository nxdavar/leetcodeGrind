class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        result = []
        intervals.sort() 
        
        for i in range(len(intervals)): 
            curr = intervals[i]
            
            index = 0
            changed = False
            while index < len(result): 
                if result[index][1] <= curr[0]: 
                    result[index] = curr
                    result.sort()
                    changed = True
                    break
                
                index += 1
            
            if not changed: 
                result.append(curr)
        
        return len(result)