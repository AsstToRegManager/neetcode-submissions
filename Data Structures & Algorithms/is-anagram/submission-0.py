class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in set(s):
            if s.count(i) != t.count(i) or len(s) != len(t):
                return False
        else:
            return True
        