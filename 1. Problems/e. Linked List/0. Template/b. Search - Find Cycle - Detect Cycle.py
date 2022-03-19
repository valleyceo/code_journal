def hasCycle(self, head: ListNode) -> bool:
    if head == None or head.next == None:
        return False

    slow = head
    fast = head.next

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast.val == slow.val:
            return True

    return False
