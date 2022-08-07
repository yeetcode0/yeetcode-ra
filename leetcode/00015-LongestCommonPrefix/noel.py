from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> int:
        max_possible_length = min([len(x) for x in strs])
        for i in range(max_possible_length):
            char = strs[0][i]
            for str in strs:
                if char != str[i]:
                    return i
        return max_possible_length


s = Solution()


print(s.longestCommonPrefix(["flower", "flow", "flight"]))
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == 2
