class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # initialse our pointers 
        p1 = m - 1
        p2 = n - 1
        p = n + m - 1
        
        # base case
        if n == 0:
            return
            
        # standard case
        else:
            while p >= 0:
                if (p1 >= 0 and nums1[p1] > nums2[p2]) or p2 < 0:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
                p -= 1