class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            count = max(count, r - l + 1)
        
        return count
            
            