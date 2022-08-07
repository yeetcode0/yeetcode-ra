from typing import *

##
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        length_nums = len(nums)
        boundary = length_nums - 2
        index_a = 0

        nearest_epsilon = None
        while index_a < boundary:
            target_b_and_c = target - nums[index_a]

            index_b = index_a + 1
            index_c = length_nums - 1

            while index_b < index_c:
                actual_b_and_c = nums[index_b] + nums[index_c]
                epsilon = actual_b_and_c - target_b_and_c

                if epsilon == 0:
                    return target

                if nearest_epsilon is None or abs(epsilon) < abs(nearest_epsilon):
                    nearest_epsilon = epsilon

                if epsilon < 0:
                    index_b += 1
                else:
                    index_c -= 1

            index_a += 1

        return target + nearest_epsilon
