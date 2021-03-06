package main

import "strings"

/*

    This problem is from https://leetcode.com

	https://leetcode.com/problems/rotate-string/

*/

func rotateString(A, B string) bool {
	if len(A) != len(B) {
		return false
	}
	return strings.Contains(A+A, B)
}

func main() {

	println(rotateString("abcde", "abced"))
}
