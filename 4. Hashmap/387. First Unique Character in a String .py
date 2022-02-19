import math

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for index, c in enumerate(s):
            if not c in hashmap.keys():
                hashmap[c] = index
            else:
                hashmap[c] = None
        unique_index = math.inf
        for k,v in hashmap.items():
            if v is not None and v < unique_index:
                unique_index = v
        return -1 if unique_index == math.inf else unique_index

if __name__ == '__main__':
    s = Solution()
    assert s.firstUniqChar('leetcode') == 0
    assert s.firstUniqChar('loveleetcode') == 2
    assert s.firstUniqChar('aabb') == -1