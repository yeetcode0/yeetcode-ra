from typing import *


ints = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def multiplier(self, this_roman: str, prev_roman: str) -> int:
        if (this_roman == "D" or this_roman == "M") and prev_roman == "C":
            return -1
        if (this_roman == "L" or this_roman == "C") and prev_roman == "X":
            return -1
        if (this_roman == "X" or this_roman == "V") and prev_roman == "I":
            return -1

        return 1

    def romanToInt(self, s: str) -> int:
        sum = 0

        next_mult = 1
        for i in range(len(s) - 1, -1, -1):
            if i == 0:
                sum += next_mult * ints[s[i]]
            else:
                term = next_mult * ints[s[i]]
                sum += term
                next_mult = self.multiplier(s[i], s[i - 1])
        return sum
