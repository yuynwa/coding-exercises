#!/use/bin/env python
# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, data, next):
        self.data = data
        self.next = next


def removeDuplicates(head):

    if head == None:
        return None

    curr = head

    while curr.next != None:

        next = curr.next
        data = curr.data

        if next.data == data:

            # this is where actual removing happens
            curr.next = next.next

            # for serial duplicate-values
            continue

        curr = next

    return head


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



if __name__ == '__main__':

    l = list()

    values = [1,2,2,3,3,3,4,4,5,6,6,7,7,8,9]

    for i in range(0, len(values)):
        n = ListNode(values[i], None)

        if i != 0:
            l[-1].next = n
        l.append(n)

    # Before
    log_nodes_throw_next_pointer(l[0])

    # Remove
    removeDuplicates(l[0])

    # After
    log_nodes_throw_next_pointer(l[0])
