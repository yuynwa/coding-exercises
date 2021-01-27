#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/sort-colors/
    
"""


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    left, move, end = 0, 0, len(nums)-1

    while move <= end:
        if nums[move] == 0:
            nums[left],nums[move] = nums[move],nums[left]
            move = move+1
            left = left+1

        elif nums[move] == 1:
            move = move+1
        else:
            nums[move],nums[end] = nums[end],nums[move]
            end = end-1
    print(nums)

if __name__ == '__main__':
    sortColors([2,1,2,2,0,1,0,0,1,2,1,2,1,1,0,0,1,0])





