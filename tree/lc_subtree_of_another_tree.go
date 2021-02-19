package main

/*

    This problem is from https://leetcode.com

    https://leetcode.com/problems/subtree-of-another-tree/

*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSubtree(s *TreeNode, t *TreeNode) bool {

	if t == nil {
		return true
	}

	if s == nil {
		return false
	}

	return isSame(s, t) || isSubtree(s.Left, t) || isSubtree(s.Right, t)
}


func isSame(s *TreeNode, t *TreeNode) bool {

	if s == nil && t == nil {
		return true
	}

	if s == nil || t == nil {
		return false
	}

	return s.Val == t.Val && isSame(s.Left, t.Left) && isSame(s.Right, t.Right)
}
