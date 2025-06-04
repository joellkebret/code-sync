from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequency = Counter(nums)

        for num, freq in frequency.items():
            heapq.heappush(heap,(freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]