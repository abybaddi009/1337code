class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for n in nums1:
            if n not in hashmap.keys():
                hashmap[n] = 0
        for n in nums2:
            if n in hashmap.keys():
                hashmap[n] = 1
        return [k for k,v in hashmap.items() if v==1]