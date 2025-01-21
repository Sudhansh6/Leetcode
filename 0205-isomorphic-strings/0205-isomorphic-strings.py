class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        map = dict()
        rev_map = dict()
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in rev_map:
                    return False
                map[s[i]] = t[i]
                rev_map[t[i]] = s[i]
            elif map[s[i]] != t[i]:
                return False
        
        return True