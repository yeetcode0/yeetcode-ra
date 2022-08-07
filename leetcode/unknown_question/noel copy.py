from typing import *


class Solution:
    def _longest(self, s: str, index_left: int, index_right: int):

        length_s = len(s)
        while 0 <= index_left and index_right < length_s:
            value_left = s[index_left]
            value_right = s[index_right]
            if value_left != value_right:
                break
            index_left -= 1
            index_right += 1

        length_p = (index_right - 1) - (index_left + 1) + 1

        return length_p

    def longestPalindrome(self, s: str) -> int:

        length_s = len(s)

        if length_s == 1:
            return 1
        max_length = -1
        for i in range(length_s):
            length_p_1 = self._longest(s, i, i)
            length_p_2 = self._longest(s, i, i + 1)
            max_length = max([max_length, length_p_1, length_p_2])
        return max_length


s = Solution()


assert s.longestPalindrome("a") == 1
assert s.longestPalindrome("ab") == 1
assert s.longestPalindrome("aba") == 3
assert s.longestPalindrome("abba") == 4
assert s.longestPalindrome("abccccdd") == 4
