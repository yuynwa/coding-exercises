package main

import (
	"fmt"
)
/*

	This problem is from https://leetcode.com

    https://leetcode.com/problems/remove-linked-list-elements/

*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//type ListNode struct {
//	Val int
//	Next *ListNode
//}

func removeElements(head *ListNode, val int) *ListNode {

	for head != nil && head.Val == val {
		head = head.Next
	}

	if head == nil {
		return head
	}

	newHead := head
	curr := head.Next
	next := newHead
	for curr != nil {

		if curr.Val != val {
			next.Next = curr
			next = next.Next
		}
		curr = curr.Next
	}

	// the last node.next = nil
	next.Next = nil
	return newHead
}

func main() {

	l5 := ListNode{Val:2}
	l4 := ListNode{Val:4, Next:&l5}
	l3 := ListNode{Val:3, Next:&l4}
	l2 := ListNode{Val:2, Next:&l3}
	l1 := ListNode{Val:1, Next:&l2}
	//fmt.Println(l1.Val)


	head := removeElements(&l1, 2)


	fmt.Println("Start")

	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}

}
