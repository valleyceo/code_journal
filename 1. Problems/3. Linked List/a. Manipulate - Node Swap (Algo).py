# Node Swap

'''
Given a head of singly linked list, make a swap for every pairs

Input:
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5

Output:
1 -> 0 -> 3 -> 2 -> 5 -> 4

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

# O(n) time | O(1) space
def nodeSwap(head):
    res = LinkedList(0)
	res.next = head
	prev = res
	
	while prev.next and prev.next.next:
		first = prev.next
		second = prev.next.next
		
		first.next = second.next
		second.next = first
		prev.next = second
		
		prev = first
	
	return res.next