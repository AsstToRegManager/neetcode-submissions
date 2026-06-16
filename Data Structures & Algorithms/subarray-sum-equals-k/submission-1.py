class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        count = sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in d:
                count += d[sum - k]
            d[sum] += 1
        
        return count