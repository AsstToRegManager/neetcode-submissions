class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in d:
                for v in d[nums[i]]:
                    print(d)
                    if abs(i - v) <= k:
                        print(i - v, " ", i, " ", v)
                        return True
            d[nums[i]].append(i)
        return False 