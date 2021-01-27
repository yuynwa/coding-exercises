package main

import "fmt"

/*

This problem is from https: //www.hackerrank.com/

https://www.hackerrank.com/challenges/ctci-array-left-rotation

SCORE: 20.0

*/

// Complete the rotLeft function below.
func rotLeft(a []int32, d int32) []int32 {
	cnt := len(a)

	reverse(a[0:d])
	reverse(a[d:cnt])
	reverse(a)
	return a
}

func reverse(a []int32) []int32 {

	cnt := len(a) - 1


	if cnt < 1 {
		return a
	}
	for i := 0; i <= cnt/2; i++ {
		a[i], a[cnt-i] = a[cnt-i], a[i]
	}
	return a
}


func main() {

	arr := []int32{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	r := int32(9)
	result := rotLeft(arr, r)

	fmt.Printf("After perform %d left rotations, the result is: %v", r, result)
}
