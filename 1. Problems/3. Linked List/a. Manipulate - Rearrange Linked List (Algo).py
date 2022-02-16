# Rearrange Linked List

'''
Given a head of linked list and a value k, rearrange the list in place such that nodes smaller than k is on the left and larger than k is on the right.

Input:
head = 3 -> 0 -> 5 -> 2 -> 1 -> 4
k = 3

Output:
0 -> 2 -> 1 -> 3 -> 5 -> 4

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

# O(n) time | O(1) space
def rearrangeLinkedList(head, k):
    smallHead, smallTail = None, None
	equalHead, equalTail = None, None
	largeHead, largeTail = None, None
	curr = head

	while curr:
		if curr.value < k:
			smallHead, smallTail = insertLL(smallHead, smallTail, curr)
		elif curr.value == k:
			equalHead, equalTail = insertLL(equalHead, equalTail, curr)
		else:
			largeHead, largeTail = insertLL(largeHead, largeTail, curr)

		temp = curr
		curr = curr.next
		temp.next = None

	smallEqHead, smallEqTail = connectLL(smallHead, smallTail, equalHead, equalTail)
	return connectLL(smallEqHead, smallEqTail, largeHead, largeTail)[0]

def insertLL(head, tail, node):
	newHead = head
	newTail = node

	if newHead is None:
		newHead = node

	if tail:
		tail.next = node

	return (newHead, newTail)

def connectLL(head1, tail1, head2, tail2):
	newHead = head2 if head1 is None else head1
	newTail = tail1 if tail2 is None else tail2

	if tail1:
		tail1.next = head2

	return (newHead, newTail)
