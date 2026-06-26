class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l + 1 >= k:
            if r - l + 1 == k:
                return arr[l : r + 1]
            elif abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1