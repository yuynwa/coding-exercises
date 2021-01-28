
package main

import (
	"fmt"
	"math"
)

/*

    This problem is from https://www.leetcode.com/

	https://leetcode.com/problems/squares-of-a-sorted-array/

*/

func sortedSquares(nums []int) []int {

	results := make([]int, len(nums))
	left, right := 0, len(nums) - 1

	for left <= right {

		n1 := math.Abs(float64(nums[left]))
		n2 := math.Abs(float64(nums[right]))

		if n1 > n2 {
			results[right-left] = int(n1 * n1)
			left++
		} else {
			results[right-left] = int(n2 * n2)
			right--
		}
	}

	return results
}

func main() {

	nums := []int {0,3,10}
	fmt.Println(sortedSquares(nums))

	nums = []int {-7,-3,2,3,11}
	fmt.Println(sortedSquares(nums))

	nums = []int {-7,-3}
	fmt.Println(sortedSquares(nums))

	nums = []int {-7}
	fmt.Println(sortedSquares(nums))

	nums = []int {-5,-3,-2,-1}
	fmt.Println(sortedSquares(nums))

	nums = []int {-5,-3,0,1}
	fmt.Println(sortedSquares(nums))

	nums = []int {-3,0,3,3,3,3,3,3}
	fmt.Println(sortedSquares(nums))

	nums = []int {-3,-3,-2,1}
	fmt.Println(sortedSquares(nums))
}
