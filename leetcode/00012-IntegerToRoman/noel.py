from typing import *


class Solution:
    def onesToRoman(self, num: int) -> int:

        romans = []
        while num > 0:
            if num == 4:
                romans.append("IV")
                num -= 4
            elif num == 9:
                romans.append("IX")
                num -= 9
            elif num == 5 or num > 5:
                romans.append("V")
                num -= 5
            else:
                romans.append("I")
                num -= 1
        return "".join(romans)

    def tensToRoman(self, num: int) -> int:
        num = int(num // 10)
        romans = []
        while num > 0:
            if num == 4:
                romans.append("XL")
                num -= 4
            elif num == 9:
                romans.append("XC")
                num -= 9
            elif num == 5 or num > 5:
                romans.append("L")
                num -= 5
            else:
                romans.append("X")
                num -= 1
        return "".join(romans)

    def hundredsToRoman(self, num: int) -> int:
        num = int(num // 100)
        romans = []
        while num > 0:
            if num == 4:
                romans.append("CD")
                num -= 4
            elif num == 9:
                romans.append("CM")
                num -= 9
            elif num == 5 or num > 5:
                romans.append("D")
                num -= 5
            else:
                romans.append("C")
                num -= 1
        return "".join(romans)

    def thousandsToRoman(self, num: int) -> int:
        num = int(num // 1000)
        romans = []
        while num > 0:

            romans.append("M")
            num -= 1
        return "".join(romans)

    def intToRoman(self, num: int) -> str:
        romans = []
        if num >= 1000:
            roman = self.thousandsToRoman(num)
            romans.append(roman)
            num = int(num % 1000)
        if num >= 100:
            roman = self.hundredsToRoman(num)
            romans.append(roman)
            num = int(num % 100)
        if num >= 10:
            roman = self.tensToRoman(num)
            romans.append(roman)
            num = int(num % 10)

        roman = self.onesToRoman(num)
        romans.append(roman)
        num = int(num // 10)

        return "".join(romans)


s = Solution()
assert s.intToRoman(0) == ""

assert s.intToRoman(1) == "I"
assert s.intToRoman(3) == "III"
assert s.intToRoman(4) == "IV"

assert s.intToRoman(5) == "V"
assert s.intToRoman(6) == "VI"
assert s.intToRoman(9) == "IX"
assert s.intToRoman(10) == "X"
assert s.intToRoman(11) == "XI"


assert s.intToRoman(12) == "XII"
assert s.intToRoman(14) == "XIV"
assert s.intToRoman(15) == "XV"
assert s.intToRoman(16) == "XVI"
assert s.intToRoman(19) == "XIX"
assert s.intToRoman(50) == "L"
assert s.intToRoman(100) == "C"
assert s.intToRoman(500) == "D"
assert s.intToRoman(1994) == "MCMXCIV"
assert s.intToRoman(1000) == "M"
