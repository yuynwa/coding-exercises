package main

import "fmt"

/*

    This problem is from https://leetcode.com

    https://leetcode.com/problems/maximum-binary-tree/

*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
	return rootNode(nums, 0, len(nums))
}


func rootNode(nums []int, left, right int) *TreeNode {

	// parent node has no left or right sub tree
	if left == right {
		return nil
	}

	maxIdx := left
	for i := left+1;i < right; i++ {
		if nums[i] > nums[maxIdx] {
			maxIdx = i
		}
	}

	node := TreeNode{Val:nums[maxIdx]}
	node.Left = rootNode(nums, left, maxIdx)
	node.Right = rootNode(nums, maxIdx+1, right)

	return &node
}

func main() {

	nums := []int{3,2,1,6,0,5}
	nums = []int{3,2,1}
	r := constructMaximumBinaryTree(nums)
	fmt.Println(r)
}
