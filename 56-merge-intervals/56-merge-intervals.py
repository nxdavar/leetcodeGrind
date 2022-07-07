class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: 
            return intervals
        
        result = []
        intervals.sort()
        result.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[len(result) - 1][1]: 
                result[len(result) - 1][1] = max(intervals[i][1], result[len(result) - 1][1])
            else:
                result.append(intervals[i])
        
        return result