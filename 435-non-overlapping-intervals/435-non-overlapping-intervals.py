class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()    
        result = 0
        index = 0
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if last_end > intervals[i][0]:
                result += 1
                last_end = min(intervals[i][1], last_end)
            else:
                last_end = intervals[i][1]
            
        return result