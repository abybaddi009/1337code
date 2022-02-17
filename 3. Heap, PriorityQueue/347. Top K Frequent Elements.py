import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = [(-v,k) for k, v in Counter(nums).items()]
        heapq.heapify(array)
        items = heapq.nsmallest(k, array)
        return [k for v, k in items]