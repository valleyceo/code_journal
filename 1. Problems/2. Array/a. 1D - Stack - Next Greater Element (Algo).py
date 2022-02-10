# Next greater element

'''
Input: array of integers
Output: next greater element for each x[i]
'''

def nextGreaterElement(array):
    res = [-1] * len(array)
	stack = []
	
	for i in range(2 * len(array)):
		idx = i % len(array)
		
		while len(stack) > 0 and array[stack[-1]] < array[idx]:
			top = stack.pop()
			res[top] = array[idx]
		
		stack.append(idx)
	
	return res