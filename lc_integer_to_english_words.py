"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/valid-parentheses/
    
"""

#
# class Solution:
#     def numberToWords(self, num: int) -> str:
#
#         if num == 0:
#             return "Zero"
#
#         to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
#         tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
#
#         def lessThanThousand(num):
#
#             ret = ""
#             while num > 0:
#
#                 if num > 99:
#                     a = int(num / 100)
#                     ret = to19[a - 1] + " Hundred"
#
#
#                 elif num > 19:
#                     a = int(num / 10)
#
#                     if len(ret) > 0:
#                         ret = ret + " " + tens[a - 2]
#                     else:
#                         ret = ret + tens[a - 2]
#
#                     num = num % 10
#                 else:
#
#                     if len(ret) > 0:
#                         ret = ret + " " + to19[num - 1]
#                     else:
#                         ret = ret + to19[num - 1]
#
#                     break
#             else:
#                 return "Zero" if len(ret) < 1 else ret
#             return ret
#
#         numStr = str(num)
#         while len(numStr) % 3 != 0:
#             numStr = "0" + numStr
#
#         l = [numStr[i:i + 3] for i in range(0, len(numStr), 3)]
#
#         if len(l) > 3:
#             zeros = [" Billion", " Million", " Thousand", ""]
#         elif len(l) > 2:
#             zeros = [" Million", " Thousand", ""]
#         elif len(l) > 1:
#             zeros = [" Thousand", ""]
#         else:
#             zeros = [""]
#
#         final = ""
#         for idx, val in enumerate(l):
#
#             n = int(val)
#
#             if n == 0:
#                 continue
#
#             sub = lessThanThousand(n)
#
#             final = final + sub + zeros[idx] + " "
#
#         if final.endswith('Zero'):
#             final = final[:-4]
#
#         return final.strip()
#


class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def lessThanThousand(num):

            ret = ""
            while num > 0:

                if num > 99:
                    a = int(num / 100)
                    num = num % 100

                    ret = to19[a - 1] + " Hundred" + lessThanThousand(num)


                elif num > 19:
                    a = int(num / 10)

                    if len(ret) > 0:
                        ret = ret + " " + tens[a - 2]
                    else:
                        ret = ret + tens[a - 2]

                    num = num % 10
                    ret = ret + lessThanThousand(num)

                else:

                    if len(ret) > 0:
                        ret = ret + " " + to19[num - 1]
                    else:
                        ret = ret + to19[num - 1]

                    break
            else:
                return "Zero" if len(ret) < 1 else ret
            return ret

        numStr = str(num)
        while len(numStr) % 3 != 0:
            numStr = "0" + numStr

        l = [numStr[i:i + 3] for i in range(0, len(numStr), 3)]

        if len(l) > 3:
            zeros = [" Billion", " Million", " Thousand", ""]
        elif len(l) > 2:
            zeros = [" Million", " Thousand", ""]
        elif len(l) > 1:
            zeros = [" Thousand", ""]
        else:
            zeros = [""]

        final = ""
        for idx, val in enumerate(l):

            n = int(val)

            if n == 0:
                continue

            sub = lessThanThousand(n)

            final = final + sub + zeros[idx] + " "

        if final.endswith('Zero'):
            final = final[:-4]

        return final.strip()



if __name__ == '__main__':

    print(Solution().numberToWords(10000060))




