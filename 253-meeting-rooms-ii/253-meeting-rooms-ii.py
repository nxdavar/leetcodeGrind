class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        result = []
        intervals.sort() 
        
        for i in range(len(intervals)): 
            curr = intervals[i]   
            changed = False
            if len(result) > 0 and result[0] <= curr[0]: 
                result[0] = curr[1]
                result.sort()
                changed = True
            
            if not changed: 
                result.append(curr[1])
                result.sort()
    
        # print(result)
        return len(result)