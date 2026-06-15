class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in range(len(nums)):
            d[nums[i]] += 1
        
        maxHeap = []

        for key, v in d.items():
            heapq.heappush(maxHeap, (-v, key))

        l = []
        for i in range(k):
            l.append(heapq.heappop(maxHeap)[1])

        return l
