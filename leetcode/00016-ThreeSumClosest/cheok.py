from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_diff = float("inf")
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target_diff = target - nums[i] - nums[l] - nums[r]
                if target_diff == 0:
                    return target

                if abs(target_diff) < abs(smallest_diff):  #
                    smallest_diff = target_diff

                if target_diff > 0:
                    l += 1
                else:
                    r -= 1

        return target - smallest_diff
