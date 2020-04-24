#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://techdevguide.withgoogle.com
    /paths/foundational/find-longest-word-in-dictionary-
    that-subsequence-of-given-string#code-challenge


    For example, given the input of S = "abppplee"
    and D = {"able", "ale", "apple", "bale", "kangaroo"}
    the correct output would be "apple"

"""

if __name__ == '__main__':

    sequence = "abppplee"
    words = {"able", "ale", "apple", "bale", "kangaroo"}

    cnt = 0
    s = ""

    for word in words:

        # a b b c
        z = word
        for idx, c in enumerate(sequence):

            if z[0] == c:
                z = z[1:]

            if len(z) == 0:

                if len(word) > len(s):
                    s = word
                    cnt = len(word)
                break


    print(str(cnt) + ", and s is`", s+"`" + "s.length =" + str(len(s)))




