from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> int:

        d = dict()
        length_s = len(s)
        for i in range(length_s):

            try:
                d[s[i]] += 1
            except:
                d[s[i]] = 1
        have_odd = False
        pairs = 0

        for values in d.values():
            pairs += int(values // 2)
            have_odd = have_odd or values % 2 == 1

        return pairs * 2 + (1 if have_odd else 0)


s = Solution()

print(s.longestPalindrome("abccccdd"))
assert s.longestPalindrome("abccccdd") == 7
