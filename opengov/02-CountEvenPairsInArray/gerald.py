from typing import *


def sum_even(A, index_left, index_right):
    value_left = A[index_left]
    value_right = A[index_right]
    return value_left % 2 == value_right % 2


def solution(A: List[int]) -> int:
    output = index = 0
    zero_used = False

    while index <= len(A) - 1:
        if index == len(A) - 1 and not zero_used and sum_even(A, index, 0):
            output += 1
            index += 1

        elif index != len(A) - 1 and sum_even(A, index, index + 1):
            if index == 0:
                zero_used = True
            output += 1
            index += 1

        index += 1
    return output


print(solution([4, 2, 4]))
print(solution([4, 2, 5, 8, 7, 3, 71]))
