package main

import "fmt"

/*

	This problem is from https://leetcode.com

    https://leetcode.com/problems/intersection-of-two-linked-lists/

*/

//type ListNode struct {
//	Val int
//	Next *ListNode
//}


func partition(head *ListNode, x int) *ListNode {

	bigger := ListNode{0, nil}
	biggerN := &bigger
	curr := head

	smaller := ListNode{0, nil}
	smallerN := &smaller

	for curr != nil {
		if curr.Val >= x {
			biggerN.Next = curr
			biggerN = curr
		} else {
			smallerN.Next = curr
			smallerN = curr
		}
		curr = curr.Next
	}

	if &biggerN != nil {
		biggerN.Next = nil
	}

	if &bigger != nil {
		smallerN.Next = bigger.Next
	}

	return smaller.Next
}

func main() {

	l1 := []int {1,4,3,2,5,2}
	n1 := NodeList(l1)

	head := partition(n1, 0)
	fmt.Println(head)
}

//
//func NodeList(nums []int ) *ListNode1 {
//
//	head := ListNode1{1, nil}
//	next := head
//	for i := 1; i < len(nums); i++ {
//		node := ListNode1{nums[i], nil}
//		next.Next = &node
//		next = node
//	}
//	return &head
//}
//func PrintLinkedList(head *ListNode1 ) {
//
//	tmp := head
//	for tmp != nil {
//		fmt.Println(tmp.Val)
//		tmp = tmp.Next
//	}
//}
