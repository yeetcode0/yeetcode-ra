from typing import *


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            count += self.search_pair(nums, target - nums[i], i)
        return count

    def search_pair(self, nums, target_sum, i):
        count = 0
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target_sum:
                count += r - l
                l += 1
            else:
                r -= 1
        return count
