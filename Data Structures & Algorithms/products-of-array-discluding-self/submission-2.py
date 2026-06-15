class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total *= num

        res = []

        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)

        return res