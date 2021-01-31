package main

/*

    This problem is from https://leetcode.com

    https://leetcode.com/problems/daily-temperatures/

*/

import (
	"fmt"
)

func dailyTemperatures(T []int) []int {

	var stack []int
	result := make([]int, len(T))

	for i, n := range T {
		for len(stack) > 0 {

			topIdx := stack[len(stack)-1]

			if n > T[topIdx] {
				stack = stack[:len(stack)-1]
				result[topIdx] = i - topIdx
			} else {
				break
			}
		}

		stack = append(stack, i)
	}

	return result
}


func main() {

	nums := []int {73, 74, 75, 71, 69, 72, 76, 73}
	result := dailyTemperatures(nums)
	fmt.Println(result)
}
