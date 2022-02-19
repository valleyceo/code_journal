# Even-Odd Merge

'''
- Given a singly linked list
- Reorder the list such that the list is ordered in following:

Input:
L -> L0 -> L1 -> L2 -> L3 -> L4

Output:
L -> L0 -> L2 -> L4 -> L1 -> L3
'''
# O(n) time | O(1) space
def even_odd_merge(L: ListNode) -> Optional[ListNode]:

    if L is None:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1  # Alternate between even and odd.
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next
