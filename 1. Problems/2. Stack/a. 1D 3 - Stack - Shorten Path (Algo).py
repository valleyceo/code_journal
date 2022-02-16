# Given a string of unix path, return the shortest path

'''
Input:
"/foo/../test/../test/../foo//bar/./baz"

Output:
"/foo/bar/baz"
'''

def shortenPath(path):
    pList = path.split('/')
	stack = [""] if path[0] == "/" else []
	
	for p in pList:
		if p == "..":
			if len(stack) == 0 or stack[-1] == "..":
				stack.append(p)
			elif stack[-1] != "":
				stack.pop()
		elif p == "" or p == ".":
			continue
		else:
			stack.append(p)
	
	if len(stack) == 1 and stack[0] == "":
		return "/"
	
	return "/".join(stack)