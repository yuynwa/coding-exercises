package main

/*

    This problem is from https://leetcode.com

	https://leetcode.com/problems/valid-anagram/

*/

func reverseWords(s string) string {

	if len(s) == 0 {
		return s
	}

	chars := []rune(s)
	cur, prevCharIsSpace := 0, true

	// remove redundant space
	for _ ,c := range chars {

		if string(c) != " " {
			chars[cur] = c
			prevCharIsSpace = false
			cur++
		} else if !prevCharIsSpace {
			chars[cur] = c
			prevCharIsSpace = true
			cur++
		}
	}

	// in case of last char is space
	fixLength := cur
	if prevCharIsSpace {
		fixLength--
	}
	if fixLength < 0 {
		return ""
	}

	chars = chars[:fixLength]

	// reverse string, `hello world` -> `dlrow olleh`
	reverse(chars, 0, len(chars))

	prevSpaceIdx := -1
	for idx, c := range chars {
		if string(c) == " " {
			reverse(chars, prevSpaceIdx + 1, idx)
			prevSpaceIdx = idx
		}
	}

	// reverse last word
	reverse(chars, prevSpaceIdx + 1, len(chars))

	return string(chars)
}


// reverse chars[start, end)
func reverse(chars []rune, start, end int) {

	end--
	for start < end {
		chars[start], chars[end] = chars[end], chars[start]
		start++
		end--
	}

}


func main() {

	println(reverseWords("the sky is blue"))
	println(reverseWords("  hello world  "))
	println(reverseWords("a good   example"))
	println(reverseWords("  Bob    Loves  Alice   "))
	println(reverseWords("Alice does not even like bob"))
	println(reverseWords(""))
	println(reverseWords("  "))
}
