from typing import *



class Solution:


    def twoSum(self, input: List[int], index_start: int, index_end: int, target: int) -> List[tuple[int,int]]:

        b_and_c_indexes_list = []

        x = set()
        while index_start < index_end:
            sum = input[index_start] + input[index_end]
            if sum < target:
                index_start += 1
            elif target < sum:
                index_end -= 1
            else:
                start_val = input[index_start]
                end_val = input[index_end]
                if start_val not in x:
                    b_and_c_indexes_list.append((start_val,end_val))

                    x.add(start_val)
                    x.add(end_val)
                index_end -= 1
                index_start += 1

        return b_and_c_indexes_list

    def threeSum(self, input: List[int]) -> List[List[int]]:
        input.sort()
        input_length = len(input)
        last_index = input_length - 1
        boundary = input_length - 2

        cursor = 0

        soln_set = []
        while cursor < boundary:
            if cursor > 0 and input[cursor - 1] == input[cursor]:
                pass
            else:
                a = input[cursor]
                sum = (-a)
                b_and_c_list = self.twoSum(input,cursor + 1, last_index,sum)
                for (b,c) in b_and_c_list:
                    soln_set.append([a,b, c])
            cursor += 1

        return soln_set

s = Solution()

s.threeSum([0,1,2])
s.threeSum([-1,0,1,2,-1,-4])



