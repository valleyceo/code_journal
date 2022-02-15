# Zip Linked List

'''
Given head of singly linked list, return a linked list in following order:

1st node -> kth node -> 2nd node -> k-1th node -> 3rd node -> ...

Input:
LL = 1 -> 2 -> 3 -> 4 -> 5 -> 6

Output:
1 -> 6 -> 2 -> 5 -> 3 -> 4

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
'''
"fdsklfjsdklfj"

# O(n) time | O(1) space
def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
		return linkedList

	firstHalf = linkedList
	secondHalf = splitLL(linkedList)
	reversedSecondHalf = reverseLL(secondHalf)

	return interweaveLL(firstHalf, reversedSecondHalf)

def interweaveLL(head1, head2):
	curr1 = head1
	curr2 = head2

	while curr1 and curr2:
		next1 = curr1.next
		next2 = curr2.next

		curr1.next = curr2
		curr2.next = next1

		curr1 = next1
		curr2 = next2

	return head1

def reverseLL(head):
	prev = None
	curr = head

	while curr:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp

	return prev

def splitLL(head):
	slow = head
	fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	secondHalf = slow.next
	slow.next = None
	return secondHalf
