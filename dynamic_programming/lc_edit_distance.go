package main

import (
	"fmt"
	"math"
)

/*

	This problem is from https://leetcode.com

    https://leetcode.com/problems/edit-distance/

*/


func minDistance(word1 string, word2 string) int {

	if len(word1) == 0 {
		return len(word2)
	}
	if len(word2) == 0 {
		return len(word1)
	}

	dp := make([][]int, len(word1)+1)
	for i := range dp {
		dp[i] = make([]int, len(word2)+1)
	}
	dp[0][0] = 0

	// 1st row
	for i:= 1; i <= len(word2); i++ {
		dp[0][i] = i
	}

	// 1st col
	for i:= 1; i <= len(word1); i++ {
		dp[i][0] = i
	}

	// other rows & cols
	for i:= 1; i <= len(word1); i++ {
		for j:= 1; j <= len(word2); j++ {

			top := dp[i-1][j] + 1
			left := dp[i][j-1] + 1
			leftTop := dp[i-1][j-1]

			if word1[i-1] != word2[j-1] {
				leftTop++
			}

			tmp := math.Min(float64(top), float64(left))
			dp[i][j] = int(math.Min(tmp, float64(leftTop)))
		}
	}
	return dp[len(word1)][len(word2)]
}


func main() {

	s1, s2 := "horse", "ros"
	fmt.Println(minDistance(s1, s2))

	s1, s2 = "intention", "execution"
	fmt.Println(minDistance(s1, s2))

}
