#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://leetcode.com

    https://leetcode.com/problems/longest-common-subsequence/


    Given two strings text1 and text2, return the length of their longest common subsequence.

    A subsequence of a string is a new string generated from the original string with some characters(can be none)
    deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
    while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

    If there is no common subsequence, return 0.

    Example 1:

        Input: text1 = "abcde", text2 = "ace"
        Output: 3
        Explanation: The longest common subsequence is "ace" and its length is 3.

    Example 2:

        Input: text1 = "abc", text2 = "abc"
        Output: 3
        Explanation: The longest common subsequence is "abc" and its length is 3.

    Example 3:

        Input: text1 = "abc", text2 = "def"
        Output: 0
        Explanation: There is no such common subsequence, so the result is 0.

    Constraints:

        1 <= text1.length <= 1000
        1 <= text2.length <= 1000
        The input strings consist of lowercase English characters only.
"""


def longestCommonSubsequence_mine(text1: str, text2: str) -> int:

    m, n = len(text1), len(text2)

    # once edit inner lists elements will effect all. same memory addr maybe
    # dp = [[0] * (n+1)] * (m+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


if __name__ == '__main__':

    text1 = "abcde"
    text2 = "ace"
    assert 3 == longestCommonSubsequence_mine(text1, text2)

    text1 = "abc"
    text2 = "abc"
    assert 3 == longestCommonSubsequence_mine(text1, text2)

    text1 = "abc"
    text2 = "def"
    assert 0 == longestCommonSubsequence_mine(text1, text2)





