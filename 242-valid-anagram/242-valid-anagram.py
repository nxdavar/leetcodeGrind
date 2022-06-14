class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_list = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)): 
            freq_list[ord(s[i]) - ord('a')] += 1
            freq_list[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(freq_list)): 
            if freq_list[i] != 0: 
                return False
        
        return True