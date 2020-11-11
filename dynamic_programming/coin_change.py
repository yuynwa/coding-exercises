#!/use/bin/env python
# -*- coding: utf-8 -*-

"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0


Example
    Example1

        Input:
        [1, 2, 5]
        11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

    Example2

        Input:
        [2]
        3
        Output: -1

"""

def coin_change_recursive(coins: list, amount: int):

    if amount == 0:
        return 0

    res = sys.maxsize

    for n in coins:

        if amount >= n:
            res = min(coin_change_recursive(coins, amount - n) + 1, res)

    return res

def coin_change_dynamic(coins: list, amount: int):

    l = [sys.maxsize for _ in range(0, amount + 1)]
    l[0] = 0


    for a in range(1, amount+1):

        for c in coins:
            if a >= c:
                l[a] = min(l[a], l[a - c] + 1)


    print(l)
    print(sys.maxsize)
    return l[-1]


if __name__ == '__main__':

    print('coin_change_recursive: ', coin_change_recursive([2,5,7], 27))
    print('coin_change_dynamic: ', coin_change_dynamic([2,5,7], 27))







