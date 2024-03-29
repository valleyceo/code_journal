# Normalize Path Names

'''
- Given a path string
- Return the shortest path
Ex:
- Input: "sc//./../tc/awk/././" -> <"tc", "ack">
- Output: "tc/ack/"
'''
# O(n) time
def shortest_equivalent_path(path: str) -> str:

    if not path:
        raise ValueError('Empty string is not a valid path.')

    path_names = []  # Uses list as a stack.
    # Special case: starts with '/', which is an absolute path.
    if path[0] == '/':
        path_names.append('/')

    for token in (token for token in path.split('/')
                  if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else:  # Must be a name.
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith('//'):]  # Avoid starting '//'.

'''
- Edge cases:
1. "/" at the beginning (special case)
2. ".."
	- "../.." and "/.." -> valid
	- {"/", ".."} -> invalid (results to "//..")
3. "///", "/./" is allowed (cd desktop///git works)
'''
