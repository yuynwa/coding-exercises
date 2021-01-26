'''
    This problem is from https://leetcode.com

    https://leetcode.com/problems/reverse-integer/description/

'''


'''

    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:

        Input: 123
        Output: 321


    Example 2:

        Input: -123
        Output: -321
    
    
    Example 3:

        Input: 120
        Output: 21
    
    Note:
        Assume we are dealing with an environment which could only store 
        integers within the 32-bit signed integer range: [−231,  231 − 1]. 
        For the purpose of this problem, assume that your function 
        returns 0 when the reversed integer overflows.

'''


class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if not isinstance(x, int):
            raise Exception('%s is not digital !' % x)

        sign = -1 if x < 0 else 1
        x = sign * x

        res = 0

        while 0 != x:
            res = res * 10 + x % 10
            if res > 2147483641:
                return 0

            x //= 10

        return sign * res


if __name__ == '__main__':

    print(Solution().reverse(10123))
    print(Solution().reverse(452423))
    print(Solution().reverse(452423))


