from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_possible_length = min([len(x) for x in strs])
        for i in range(max_possible_length):
            char = strs[0][i]
            for str in strs:
                if char != str[i]:
                    return strs[0][:i]
        return strs[0][:max_possible_length]

s = Solution()

assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"