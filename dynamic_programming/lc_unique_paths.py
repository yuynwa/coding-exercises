#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/unique-paths/

"""

'''
        
    
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    
    How many possible unique paths are there?
    
     
    Example 1:
    
        Input: m = 3, n = 7
        Output: 28
    Example 2:
    
        Input: m = 3, n = 2
        Output: 3
    Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down
    Example 3:
    
        Input: m = 7, n = 3
        Output: 28
    Example 4:
        
        Input: m = 3, n = 3
        Output: 6
     
    Constraints:
    
        1 <= m, n <= 100
        It's guaranteed that the answer will be less than or equal to 2 * 109.

'''


class Solution:


    def uniquePaths(self, row, col):

        steps = [[0] * col] * row

        print(steps)
        for r in range(0, row):
            for c in range(0, col):

                if c == 0 or r == 0:
                    steps[r][c] = 1
                else:
                    steps[r][c] = steps[r - 1][c] + steps[r][c - 1]

        return steps[r][c]
        # return steps[row - 1][col - 1] // same as above



if __name__ == '__main__':


    print(Solution().uniquePaths(3,7))
    print(Solution().uniquePaths(3,2))
    print(Solution().uniquePaths(7,3))
    print(Solution().uniquePaths(3,3))








