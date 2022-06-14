class Solution:
    def frequencySort(self, s: str) -> str:
        initial = {}
        freqMap = {}
        resultList = []
        result = []
        
        for i in range(len(s)):
            if s[i] not in initial: 
                initial[s[i]] = 0
            initial[s[i]] += 1
        
        for key in initial.keys():
            if initial[key] not in freqMap: 
                freqMap[initial[key]] = []
            curr = freqMap[initial[key]]
            curr.append(key)
            freqMap[initial[key]] = curr
        
        for key in reversed(sorted(freqMap.keys())):
            currList = freqMap.get(key)
            for i in range(len(currList)):
                resultList.append(currList[i] * key)
        
        return "".join(resultList)