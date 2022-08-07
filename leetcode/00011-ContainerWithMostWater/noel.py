from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_area = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(area, max_area)

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1

        return max_area


s = Solution()

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(s.maxArea(heights))
assert s.maxArea(heights) == 49
