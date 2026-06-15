class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums) // 3
        count = Counter(nums)
        res = []

        for k, v in count.items():
            if v > l:
                res.append(k)
        
        return res