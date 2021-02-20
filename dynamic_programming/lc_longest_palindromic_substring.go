package main

import (
	"fmt"
)

/*

	This problem is from https://leetcode.com

    https://leetcode.com/problems/longest-palindromic-substring/

*/


func longestPalindrome(s string) string {

	if len(s) < 2 {
		return s
	}

	length := len(s)

	dp := make([][]bool, length)

	for i:= 0; i< length; i++ {
		dp[i] = make([]bool, length)
	}

	for i:= 0; i< length; i++ {
		dp[i][i] = true
	}

	result := string(s[0])

	for i:= length-1; i>=0; i-- {
		for j:= i; j< length; j++ {

			if len(s[i:j]) <= 2 {
				dp[i][j] = s[i] == s[j]
			} else {
				dp[i][j] = dp[i+1][j-1] && s[i] == s[j]
			}

			if dp[i][j] && (j-i+1 > len(result)) {
				result = s[i:j+1]
			}
		}
	}

	return result
}

func main() {

	s := "babad"
	fmt.Println(longestPalindrome(s))

	s = "cbbd"
	fmt.Println(longestPalindrome(s))

	s = "a"
	fmt.Println(longestPalindrome(s))

	s = "ac"
	fmt.Println(longestPalindrome(s))

	s = "aaaa"
	fmt.Println(longestPalindrome(s))

}
