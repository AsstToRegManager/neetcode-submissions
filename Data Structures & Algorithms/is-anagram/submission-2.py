class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1, d2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1
        
        for k in d1:
            if d2[k] != d1[k]:
                return False
        
        return True