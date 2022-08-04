from typing import *


class Solution:
    def search_pair(self, nums, target_sum, l, triplets):
        r = len(nums) - 1
        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == target_sum:
                triplets.append([-target_sum, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif target_sum > current_sum:
                l += 1
            else:
                r -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.search_pair(nums, -nums[i], i + 1, triplets)
        return triplets
