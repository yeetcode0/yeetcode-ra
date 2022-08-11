class Solution:
    def longestPalindrome(self, s: str) -> int:
        # find the length of longest palindrome
        length = 0
        odd_present = False

        dict = {}

        for c in s:
            if c not in dict:
                dict[c] = 0

            dict[c] += 1

        # ccc --> #ccc
        for value in dict.values():
            is_odd = value % 2 == 1
            length += value - 1 if is_odd else value

            if is_odd:
                odd_present = True

        return length + 1 if odd_present else length
