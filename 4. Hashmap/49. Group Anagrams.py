from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            hashed = self.hashStr(word)
            if hashed not in hashmap.keys():
                hashmap[hashed] = []
            hashmap[hashed].append(word)
        return [values for k, values in hashmap.items()]
    
    def hashStr(self, string: str):
        return "".join(sorted(string))


if __name__ == '__main__':
    sol = Solution()
    output = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(output)