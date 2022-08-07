from math import log
from typing import *


class Solution:
    def isPalindrome(self, number: int) -> bool:
        original = number
        if number < 0:
            return False

        reversed_number = 0

        while number > 0:
            digit = number % 10
            number = int(number // 10)
            reversed_number = reversed_number * 10 + digit

        return reversed_number == original


s = Solution()


assert s.isPalindrome(0)
assert s.isPalindrome(9)
assert not s.isPalindrome(10)
assert not s.isPalindrome(20)
assert s.isPalindrome(202)
assert s.isPalindrome(4004)
assert s.isPalindrome(313)
assert s.isPalindrome(432101234)
