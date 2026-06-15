class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in range(len(nums)):
            d[nums[i]] += 1

        for k, v in d.items():
            if v >= len(nums) / 2:
                return k