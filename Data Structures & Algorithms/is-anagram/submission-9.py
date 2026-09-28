class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmapS = {}
        hashmapT = {}
        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1
        
        for c in s:
            if c not in hashmapT:
                return False
            elif hashmapS[c] != hashmapT[c]:
                return False
        return True
        