package main

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {

	if head == nil || head.Next == nil {
		return true
	}
	if head.Next.Next == nil {
		return head.Val == head.Next.Val
	}

	mid := middleNode(head)
	left, right := head, reverse(mid.Next)

	for right != nil {
		if right.Val != left.Val {

			// uncomment to recover structure of the original linked list.
			//reverse(right)
			return false
		}
		left = left.Next
		right = right.Next
	}
	// uncomment to recover structure of the original linked list.
	//reverse(right)
	return true
}

func middleNode(head *ListNode) *ListNode {

	if head.Next == nil {
		return head
	}

	slow := head
	fast := head

	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}


func reverse(head *ListNode) *ListNode {

	var newHead *ListNode

	for head != nil {
		tmp := head.Next
		head.Next = newHead
		newHead = head
		head = tmp
	}
	return newHead
}

func main() {

	head := NodeList([]int {1,1,2,1})
	PrintLinkedList(head)
	//PrintLinkedList(head)

	//middleNode(head)

	fmt.Println(isPalindrome(head))
	PrintLinkedList(head)

}


//func NodeList(nums []int ) *ListNode {
//
//	head := &ListNode{1, nil}
//	next := head
//	for i := 1; i < len(nums); i++ {
//		node := ListNode{nums[i], nil}
//		next.Next = &node
//		next = &node
//	}
//	return head
//}
//func PrintLinkedList(head *ListNode) {
//
//	tmp := head
//	for tmp != nil {
//		fmt.Print(tmp.Val)
//		tmp = tmp.Next
//	}
//	fmt.Println("")
//}
