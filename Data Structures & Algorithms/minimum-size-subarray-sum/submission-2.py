class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l = 0
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target and l <= r:
                minLen = min(minLen, r - l + 1)
                window_sum -= nums[l]
                l += 1
            
        return 0 if minLen == float('inf') else minLen
            
