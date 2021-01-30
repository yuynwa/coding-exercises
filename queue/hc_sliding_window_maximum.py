#!/use/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/sliding-window-maximum/
    
"""


def maxSlidingWindow(nums, k):

    if k == 1 or len(nums) == 1 or len(nums) < k:
        return nums

    deq = deque()
    result = []

    for i in range(0, len(nums)):

        while len(deq) > 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)

        # not in range of [i-k+1 i] already.
        if deq[0] < i - k + 1:
            deq.popleft()

        result.append(nums[deq[0]])

    # Remove elements added during window slide from index 0 to k-1
    return result[k-1:]


def maxSlidingWindow_2_parts(self, nums, k):

    if k == 1 or len(nums) == 1 or len(nums) < k:
        return nums

    deq = deque()
    deq.append(0)
    result = []
    for i in range(1, k):

        while len(deq) > 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)

    result.append(nums[deq[0]])

    for i in range(k, len(nums)):

        # not in range of [i-k+1 i] already.
        if deq[0] < i - k + 1:
            deq.popleft()

        while len(deq) > 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)
        result.append(nums[deq[0]])

    return result



if __name__ == '__main__':

    assert [7,7,5,3,8,8] == maxSlidingWindow([1,7,5,3,-3,-1,8,2],3)
    assert [3,3,5,5,6,7] == maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
