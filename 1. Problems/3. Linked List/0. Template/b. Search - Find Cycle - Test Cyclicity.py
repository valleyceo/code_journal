# Test Cyclicity

'''
- Check if Linked List is cyclic
'''
def has_cycle(head: ListNode) -> Optional[ListNode]:
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Finds the start of the cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # Both iterators advance in tandem.
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it  # iter is the start of cycle.
    return None  # No cycle.

'''
Floyd's algorithm
- full equation: i = m + p*n + k
- after derivation: m + k = q * n -> m = q*n - k
- time: O(n)
'''
