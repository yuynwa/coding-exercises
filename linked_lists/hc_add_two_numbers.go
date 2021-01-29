package main

import (
	"fmt"
)

/*

	This problem is from https://leetcode.com

    https://leetcode.com/problems/add-two-numbers/

*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	head := ListNode{0,nil}
	next := &head
	sum := 0

	for l1 != nil || l2 != nil {

		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		node := ListNode{sum % 10, nil}
		next.Next = &node
		next = &node
		sum = sum / 10
	}

	if 1 == sum {
		next.Next = &ListNode{1,nil}
	}
	return head.Next
}


func nodeList(l []int) *ListNode {

	var h1 *ListNode
	var next *ListNode
	for i, n := range l {
		node := ListNode{n, nil}
		if 0 == i {
			h1 = &node
		} else {
			next.Next = &node
		}
		next = &node
	}

	return h1
}


func main() {

	l1 := []int{9,9,9,9,9,9,9}
	l1 = []int{0}
	//l1 = []int{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1}
	l1 = []int{2,4,3}
	h1 := nodeList(l1)

	l2 := []int{9,9,9,9}
	//l2 = []int{0}
	l2 = []int{5,6,4}
	h2 := nodeList(l2)

	head := addTwoNumbers(h1, h2)
	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}

}
