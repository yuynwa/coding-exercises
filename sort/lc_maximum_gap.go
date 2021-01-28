/*
	This problem is from https://leetcode.com

	https://leetcode.com/problems/maximum-gap/

*/
package main

import (
	"fmt"
	"math"
)

func maximumGap(nums []int) int {

	size := len(nums)

	if 2 == size {
		return int(math.Abs(float64(nums[0] - nums[1])))
	}

	if size < 2 {
		return 0
	}

	// retrieve min and max of array
	min, max := nums[0], nums[0]

	for i := 1; i < size; i++ {
		if nums[i] > max {
			max = nums[i]
		} else if nums[i] < min {
			min = nums[i]
		}
	}

	// equal elements
	if min == max {
		return 0
	}

	gap := int(float64((max - min) / (size - 1))) + 1
	capacity := size - 1

	bucketMIN := make([]int, capacity)
	bucketMAX := make([]int, capacity)

	for i := 0; i < capacity; i++ {
		bucketMIN[i] = math.MaxInt64
		bucketMAX[i] = math.MinInt64
	}

	// buckets become
	// bucketMIN = { MaxInt64, MaxInt64, MaxInt64, ...}
	// bucketMAX = { MinInt64, MinInt64, MinInt64, ...}

	// put nums into buckets respectively
	for i := 0; i < size; i++ {

		num := nums[i]

		if num == max || num == min {
			continue
		}

		// index of buckets
		idx := (num - min) / gap

		bucketMIN[idx] = int(math.Min(float64(num), float64(bucketMIN[idx])))
		bucketMAX[idx] = int(math.Max(float64(num), float64(bucketMAX[idx])))
	}

	maxGap := math.MinInt64
	prev := min

	for i := 0; i < capacity; i++ {

		if bucketMIN[i] == math.MaxInt64 &&
			bucketMAX[i] == math.MinInt64 {

			// empty bucket
			continue
		}

		maxGap = int(math.Max(float64(maxGap), float64(bucketMIN[i] - prev)))
		prev = bucketMAX[i]

	}

	maxGap = int(math.Max(float64(maxGap), float64(max - prev)))

	return maxGap
}


func main() {

	//nums := []int {1,2,6,10,15,30}
	nums := []int {3,9,1,2}
	fmt.Print(maximumGap(nums))
}
