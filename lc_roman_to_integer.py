#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/roman-to-integer/
    
"""

if __name__ == '__main__':

    def romanToInt(s: str) -> int:


        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        idx = 0
        while idx < len(s) - 1:


            if dic[s[idx]] < dic[s[idx + 1]]:
                result += (dic[s[idx + 1]] - dic[s[idx]])
                idx += 2
            else:

                result += dic[s[idx]]
                idx += 1

        # the last step
        if idx == len(s) - 1:
            result += dic[s[-1]]

        print(result)



    romanToInt(s="MCMXCIV")





