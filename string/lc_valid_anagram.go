package main

/*

    This problem is from https://leetcode.com

	https://leetcode.com/problems/valid-anagram/

*/

func isAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	chars := make([]int, 26)

	for _, c := range s {
		chars[c - 'a'] += 1
	}

	for _, c := range t {

		chars[c - 'a'] -= 1

		if chars[c - 'a'] < 0{
			return false
		}
	}

	return true
}

func main() {

	println(isAnagram("abcde", "abced"))
	println(isAnagram("decab", "abced"))
}
