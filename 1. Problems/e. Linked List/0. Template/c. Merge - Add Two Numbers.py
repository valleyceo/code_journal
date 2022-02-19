# Add List-Based Integers

'''
- Given two singly linked list representing digits (least significant digit comes first)
- Return list of sum
- Ex:

Input
L1->3->1->4
L2->7->0->9

Output
L->0->2->3->1
'''
# O(n + n) time | O(max(n, m)) space
def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:

    place_iter = dummy_head = ListNode()
    carry = 0

    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next
    return dummy_head.next
