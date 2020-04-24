/*
    
    This problem is from https://leetcode.com

    
    Write an algorithm to determine if a number n is "happy".

    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
    
    Return True if n is a happy number, and False if not.
    
    Example: 
    
        Input: 19
        Output: true
        
        Explanation: 
            12 + 92 = 82
            82 + 22 = 68
            62 + 82 = 100
            12 + 02 + 02 = 1

*/


class Solution {

    func isHappy(_ n: Int) -> Bool {

        var s = Set<Int>()
        var next = digitSquareSum(n)

        while !s.contains(next) {

            if next < 1 {
                return false
            }
            if next == 1 {
                return true
            }

            s.insert(next)
            next = digitSquareSum(next)
        }
        return  false
    }

    func digitSquareSum(_ n: Int) -> Int {

        var n1 = n
        var remainder = n1 % 10

        var next = 0
        while n1 != 0 {
            next += (remainder * remainder)
            n1 = n1 / 10
            remainder = n1 % 10
        }
        return next
    }
}
