package main

import (
	"fmt"
	"math"
)


func maxProfit_dp(prices []int) int {

	if len(prices) < 2 {
		return 0
	}

	length := len(prices)

	deltas := make([]int, length-1)
	for i:=1; i < len(prices); i++ {
		deltas[i-1] = prices[i] - prices[i-1]
	}

	length = len(deltas)
	dp := make([]int, length)
	dp[0] = deltas[0]
	result := dp[0]

	for i:=1; i < length; i++ {

		prev := dp[i-1]

		if prev > 0 {
			dp[i] = prev+deltas[i]
		} else {
			dp[i] = deltas[i]
		}
		result = int(math.Max(float64(dp[i]), float64(result)))
	}

	if result < 0 {
		return 0
	}
	return result
}

func maxProfit(prices []int) int {

	if len(prices) < 2 {
		return 0
	}

	min, max := prices[0], -1

	for i:=1; i < len(prices);i++ {
		if prices[i] < min {
			min = prices[i]
		}
		max = int(math.Max(float64(max), float64(prices[i] - min)))
	}

	if max < 0 {
		return 0
	}
	return max
}


func main() {
	prices := []int{7,1,5,3,6,4}
	fmt.Println(maxProfit_dp(prices))

	prices = []int{7,6,4,3,1}
	fmt.Println(maxProfit_dp(prices))

}
