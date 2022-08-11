from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        index_l = index_r = 0
        total_sub_array = 0
        min_count = None

        length_num = len(nums)
        while index_r < length_num:
            total_sub_array += nums[index_r]

            if total_sub_array >= target:
                this_length = index_r - index_l + 1
                min_count = (
                    this_length if min_count is None else min(this_length, min_count)
                )

                total_sub_array -= nums[index_l] + nums[index_r]
                index_l += 1
            else:
                index_r += 1
        return 0 if min_count is None else min_count
