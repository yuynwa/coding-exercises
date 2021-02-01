package main

/*

    This problem is from https://leetcode.com

    https://leetcode.com/problems/daily-temperatures/

*/

import (
	"fmt"
)

func dailyTemperatures(T []int) []int {

	result := make([]int, len(T))

	for i:= len(T)-2; i >= 0;i-- {
		j := i+1

		for true {
			if T[i] < T[j] {
				result[i] = j - i
				break
			} else if result[j] == 0 {
				result[i] = 0
				break
			} else if T[i] == T[j] {
				result[i] = result[j]+j-i
				break
			} else {
				j = result[j] + j
			}
		}
	}

	return result
}


func dailyTemperatures_stack(T []int) []int {

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
