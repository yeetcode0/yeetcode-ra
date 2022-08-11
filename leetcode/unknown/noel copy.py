from typing import *


class Solution:
    def _min(
        self, subtarget: int, nums: List[int], this_index: int, counted: int
    ) -> int or None:

        if this_index < 0:
            return None

        with_this_element_value = nums[this_index]
        with_this_element_remaining = subtarget - with_this_element_value
        with_this_element_count = None
        if with_this_element_remaining == 0:
            with_this_element_count = 1 + counted
        elif with_this_element_remaining <= 0:
            pass
        else:
            with_this_element_count = self._min(
                with_this_element_remaining, nums, this_index - 1, 1 + counted
            )

        without_this_element_count = self._min(subtarget, nums, this_index - 1, counted)

        if (
            with_this_element_count is not None
            and without_this_element_count is not None
        ):
            return min(with_this_element_count, without_this_element_count)
        elif without_this_element_count is None:
            return with_this_element_count
        elif with_this_element_count is None:
            return without_this_element_count
        else:
            return None

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        nums.sort()

        some = self._min(target, nums, len(nums) - 1, 0)
        return 0 if some is None else some


s = Solution()


target, nums = 7, [2, 3, 1, 2, 4, 3]


actual = s.minSubArrayLen(target, nums)

print(actual)


target, nums = 4, [1, 4, 4]


actual = s.minSubArrayLen(target, nums)

print(actual)


target, nums = 11, [1, 1, 1, 1, 1, 1, 1, 1]

actual = s.minSubArrayLen(target, nums)

print(actual)
