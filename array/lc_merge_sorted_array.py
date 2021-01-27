#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/merge-sorted-array/
    
"""


def merge(ums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    #
    idx1, idx2 = m-1, n-1
    curr = m+n-1

    while idx2 >= 0:
        n1 = nums1[idx1]
        n2 = nums2[idx2]

        # 1. idx1 < 0 indicate elements in range(0, idx2) of nums2 are smaller than nums1[0]
        # 2. idx1 < 0 nums1[curr] should from nums2
        if idx1 >= 0 and n1 > n2:
            nums1[curr] = n1
            idx1 = idx1 - 1
        else:
            nums1[curr] = n2
            idx2 = idx2 - 1
        curr = curr - 1

    print(nums1)

    # while idx2 >= 0:
    #     n1 = nums1[idx1]
    #     n2 = nums2[idx2]
    #
    #     # idx1 < 0 indicate elements in range(0, idx2) of nums2 are smaller than nums1[0]
    #     if idx1 >= 0 and n1 > n2:
    #         nums1[curr] = n1
    #         idx1 = idx1 - 1
    #     elif idx1 < 0:  # batch
    #         nums1[0:curr + 1] = nums2[0:curr + 1]
    #         return
    #     else:
    #         nums1[curr] = n2
    #         idx2 = idx2 - 1
    #
    #     curr = curr - 1


if __name__ == '__main__':
    nums1 = [2,3,4,7,0,0,0]
    # nums1=[1]
    m = len(nums1)

    nums2 = [1,5,6]
    # nums2=[]
    n = len(nums2)

    merge(nums1, m-n, nums2, n)





