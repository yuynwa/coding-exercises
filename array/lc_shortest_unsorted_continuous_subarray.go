package main

import "fmt"

/*
    
    This problem is from https://www.leetcode.com/

    https://leetcode.com/problems/shortest-unsorted-continuous-subarray
    
*/

func findUnsortedSubarray(nums []int) int {

	end := 0
	max := nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] >= max {
			max = nums[i]
		} else {
			end = i
		}
	}

	begin := 0
	min := nums[len(nums)-1]
	for i := len(nums)-1; i >= 0; i-- {
		if nums[i] <= min {
			min = nums[i]
		} else {
			begin = i
		}
	}

	if end == 0 {
		return 0
	}
	fmt.Println(begin, end)
	return end - begin + 1
}

func main() {

	nums := []int{1,2,6,4,8,10,9,15}
	//nums = []int{5,2,6,4,8,10,9,15}
	//nums = []int{1,91,15}
	//nums = []int{1}
	//nums = []int{1,1,1,1,1,1,1}
	nums = []int{1,2,3,5,4}
	fmt.Print(findUnsortedSubarray(nums))
}


