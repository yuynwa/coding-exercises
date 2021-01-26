'''
    This problem is from https://leetcode.com

    https://leetcode.com/problems/zigzag-conversion/description/

'''

'''

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
    
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int numRows);

    Example 1:

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

    Example 2:

        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:

        P     I    N
        A   L S  I G
        Y A   H R
        P     I

'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if 1 >= numRows:
            return s

        ret = ''

        foo = numRows - 1 << 1
        l = len(s)

        for i in range(numRows):

            for j in range(0, l, foo):

                idx = i + j

                if l > idx:
                    ret += s[idx]

                idx = j + foo - i

                if i != 0 and i != (numRows - 1) and l > idx:

                    ret += s[idx]

        return ret





if __name__ == '__main__':

    slt = Solution()

    assert slt.convert("PAYPALISHIRING", 3) == 'PAHNAPLSIIGYIR'
    assert slt.convert("PAYPALISHIRING", 4) == 'PINALSIGYAHRPI'



