#!/use/bin/env python
# -*- coding: utf-8 -*-

"""
    https://leetcode.com/problems/reverse-linked-list/

    https://www.hackerrank.com/challenges/reverse-a-linked-list


"""
class ListNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next


def reverse_nodes_recursion(head):
    if head == None:
        return head
    if head.next == None:
        return head

    # 5-4-3-2
    newHead = reverse_nodes_recursion(head.next)

    # 2-1
    head.next.next = head

    # 1-none
    head.next = None

    return newHead


def reverse_nodes_iterator(head):
    prev = None
    curr = head

    # 1-2-3-4-5
    while curr != None:
        # next=2
        # next=3
        next = curr.next

        # 1-none
        # 2-1-none
        curr.next = prev

        # prev=1
        # prev=2
        prev = curr

        # curr=2
        # curr=3
        curr = next


if __name__ == '__main__':

    l = list()

    for i in range(0, 5):
        n = ListNode(i, None)

        if i != 0:
            l[-1].next = n
        l.append(n)

    # reverse_nodes_recursion(l[0])

    # or
    reverse_nodes_iterator(l[0])
