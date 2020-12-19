#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
    
    https://leetcode.com/problems/linked-list-cycle/
    
"""


class ListNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next


def has_cycle(head):

    if head == None or head.next == None:
        return False

    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == '__main__':

    pass
