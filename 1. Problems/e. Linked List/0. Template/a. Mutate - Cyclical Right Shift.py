# Cyclic Shift

'''
- Given singly linked list and nonnegative integer k
- Return the list cyclically shifted to the right by k

- Can assume k < n since k = k % n
'''

# O(n) time | O(1) space
def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:

    if L is None:
        return L

    # Computes the length of L and the tail.
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L

    tail.next = L  # Makes a cycle by connecting the tail to the head.
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head
