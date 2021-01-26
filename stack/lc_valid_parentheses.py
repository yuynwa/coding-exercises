"""

    This problem is from https://leetcode.com

    https://leetcode.com/problems/valid-parentheses/

"""

"""
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
    
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    Example 1:
    
    
        Input: "()"
        Output: true
    
    Example 2:
    
        Input: "()[]{}"
        Output: true
        
        
    Example 3:
    
        Input: "(]"
        Output: false
        
        
    Example 4:
    
        Input: "([)]"
        Output: false
        
        
    Example 5:
    
        Input: "{[]}"
        Output: true
    
"""


class Solution:
    def isValid(self, s: str) -> bool:

        length = len(s)

        if length & 1 == 1:
            return False


        foo = []
        bar = {")" : "(", "]" : "[", "}" : "{"}
        keys = bar.keys()
        values = bar.values()

        for char in s:

            if char in values:
                foo.append(char)

            elif char in keys:

                if foo == [] or bar[char] != foo.pop():
                    return False
            else:
                return False


        return foo == []

if __name__ == "__main__":

    print(Solution().isValid("()[]{}"))
