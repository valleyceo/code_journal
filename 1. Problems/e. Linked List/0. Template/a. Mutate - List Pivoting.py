# List Pivoting

'''
- Given a singly linked list and a node within list with value k
- Pivot the list such that all nodes smaller than k are on left and larger than k on the right.
- Ex:
Input:
L->3->2->2->11->7->5->11
Output:
L->3->2->2->5->7->11->11
'''

# O(n) time | O(1) space
def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:

    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()
    # Populates the three lists.
    while l:
        if l.data < x:
            less_iter.next = l
            less_iter = less_iter.next
        elif l.data == x:
            equal_iter.next = l
            equal_iter = equal_iter.next
        else:  # l.data > x.
            greater_iter.next = l
            greater_iter = greater_iter.next
        l = l.next
    # Combines the three lists.
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v
