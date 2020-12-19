#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://hackerrank.com

    https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
    
"""

class ListNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next

def deleteNode(head, pos):

    if pos < 1:
        return head.next

    element = head
    p = pos

    # find prev node
    while p > 1:
        element = element.next
        p = p - 1

    if element.next != None:
        element.next = element.next.next

    return head


if __name__ == '__main__':

    l = list()


    for i in range(0, 5):
        n = ListNode(i, None)

        if i != 0:
            l[-1].next = n
        l.append(n)

    # deleteNode(head=l[0], pos=0)
    # deleteNode(head=l[0], pos=1)
    # deleteNode(head=l[0], pos=2)
    # deleteNode(head=l[0], pos=3)
    # deleteNode(head=l[0], pos=4)
    # deleteNode(head=l[0], pos=5)




