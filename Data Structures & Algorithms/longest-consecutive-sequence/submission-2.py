class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        start = []
        maxLen = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                start.append(nums[i])
            
        for st in start:
            i = 0
            currLen = 0
            while st + i in s:
                currLen += 1
                i += 1
            maxLen = max(maxLen, currLen)

        return maxLen