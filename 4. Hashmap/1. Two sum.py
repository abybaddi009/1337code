class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, two in enumerate(nums):
            one = target - two
            if one in hashmap.keys():
                return [hashmap[one], index]
            else:
                hashmap[two] = index
        return None