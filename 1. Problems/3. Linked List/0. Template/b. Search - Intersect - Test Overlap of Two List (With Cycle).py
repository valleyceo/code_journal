# Test for Overlapping List 2 (may have cycles)

'''
Given two cycle-free singly linked list
Determine if there exists a node that is common to both lists.

- each linked list may have cycles
- there can be multiple point of merge (another one after a cycle)
'''

# O(n) time | O(n) space
def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:

    # Store the start of cycle if any.
    root0, root1 = has_cycle(l0), has_cycle(l1)

    if not root0 and not root1:
        # Both lists don't have cycles.
        return overlapping_no_cycle_lists(l0, l1)
    elif (root0 and not root1) or (not root0 and root1):
        # One list has cycle, one list has no cycle.
        return None
    # Both lists have cycles.
    temp = root1
    while temp:
        temp = temp.next
        if temp is root0 or temp is root1:
            break

    # They could be both cyclic but not overlap
    return root1 if temp is root0 else None

'''
- If one list is cyclic and overlaps, the other list must be cyclic.
- If they are cycle and overlap, both lists will have same root node.
'''
