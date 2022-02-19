import heapq
import unittest

from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        """
        We heappop the minimal pair (S0, N1, N2), then immediately heappush two larger pairs (S1, N1+1,N2) and (S2, N1, N2+1).
        (why S1 and S2 always larger than S0? Because the two arrays are sorted.) 

        And right after the heappush, the heap gets re-heaped, and of course the root at this point is larger (at least equal) than (S0, N1, N2).
        Remember though, the root now maybe (S1, N1+1,N2) or (S2, N1, N2+1) or any other pair that already exists in the heap after that heappop operation. 
        This process gets repeated over and over again until finished.

        From this, we can conclude that, the pairs that get heappushed is always larger than the pairs that get heappopped earlier. It might be smaller than other pairs 
        that are currently in the heap, but we don't care about that. We only care about pairs that got pushed or popped.

        The beauty of this algorithm is, it works perfectly under the fact: two array are sorted. If the arrays were to be unsorted, we would not be able to guarantee 
        that the two pairs get heappushed are always larger than the pair that gets heappopped, thus it would be possible that a pair that gets heappopped later is larger
        than one gets heappopped ealier, which would fail to produce the correct answer.
        """
        if not nums1 or not nums2:
            return []

        visited = {}
        heap = []
        output = []

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited["0,0"] = 0

        while len(output) < k and heap:

            _, i, j = heapq.heappop(heap)
            output.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and f"{i + 1},{j}" not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited[f"{i + 1},{j}"] = 0

            if j + 1 < len(nums2) and f"{i},{j + 1}" not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited[f"{i},{j + 1}"] = 0

        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        result = self.s.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
        self.assertCountEqual(result, [[1, 2], [1, 4], [1, 6]])

    def test_two(self):
        result = self.s.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)
        self.assertCountEqual(result, [[1, 1], [1, 1]])

    def test_three(self):
        result = self.s.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3)
        self.assertCountEqual(result, [[1, 3], [2, 3]])


if __name__ == "__main__":
    unittest.main()
