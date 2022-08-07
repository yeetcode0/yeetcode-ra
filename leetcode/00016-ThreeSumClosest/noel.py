from time import monotonic_ns
from typing import *

from numpy import diff


# [ 2 , 4 ,5 , 7]


class Solution:
    def twoSumClosest(
        self, nums: List[int], index_start: int, target: int, known_closest: int
    ) -> int:
        nearest_epsilon = known_closest
        length_nums = len(nums)
        i = index_start
        j = length_nums - 1

        while i < j:
            sum = nums[i] + nums[j]

            epsilon_signed = target - sum

            if nearest_epsilon is None:
                nearest_epsilon = epsilon_signed
            elif abs(nearest_epsilon) > abs(epsilon_signed):
                nearest_epsilon = epsilon_signed
            else:
                return nearest_epsilon

            if sum < target:
                i += 1
            elif target < sum:
                j -= 1
            else:
                return nearest_epsilon

        return nearest_epsilon

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        nearest_epsilon: int or None = None
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum_target: int = target - nums[i]
            local_epsilon_signed: int = self.twoSumClosest(
                nums, i + 1, two_sum_target, nearest_epsilon
            )

            if nearest_epsilon is None:
                nearest_epsilon = local_epsilon_signed
            elif abs(nearest_epsilon) > abs(local_epsilon_signed):
                nearest_epsilon = local_epsilon_signed
            else:
                break

        return target - nearest_epsilon


s = Solution()

print(s.threeSumClosest([-1, 2, 1, -4], 1))
# assert s.threeSumClosest([-1,2,1,-4],1) == 2
