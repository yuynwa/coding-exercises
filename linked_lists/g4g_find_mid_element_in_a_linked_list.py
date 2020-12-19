#!/use/bin/env python
# -*- coding: utf-8 -*-


"""
    
    This problem is from https://practice.geeksforgeeks.org/home/

    https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
    
"""

class ListNode:

    def __init__(self, data, next):
        self.data = data
        self.next = next


def log_nodes_throw_next_pointer(head):

    if head == None:
        print("None")
        return

    curr = head
    s = str(curr.data)

    while curr != None:
        if curr.next == None:
            n = "None"
        else:
            n = str(curr.next.data)
        s = s + "->" + n
        curr = curr.next

    print(s)



def findMid(head):

    if head == None or head.next == None:
        return head.data

    fast = head.next.next

    # only 2 nodes
    if fast == None:
        return head.next.data

    slow = head

    while fast != None:

        slow = slow.next

        if fast.next == None:
            return slow.data
        if fast.next.next == None:
            return slow.next.data

        fast = fast.next.next

    return slow.data




if __name__ == '__main__':

    l = list()

    values = [1,2,3,4,5,6]

    for i in range(0, len(values)):
        n = ListNode(values[i], None)

        if i != 0:
            l[-1].next = n
        l.append(n)

    log_nodes_throw_next_pointer(l[0])

    mid = findMid(l[0])

    if mid != None:
        print("mid is " + str(mid))
    else:
        print("mid is none")

