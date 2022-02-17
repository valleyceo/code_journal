# Brackets Well-Formedness

'''
- Given a string with brackets "{,},(,),[,]"
- Check if brackets are all correctly closed.
'''
# O(N) Time
def is_well_formed(s: str) -> bool:

    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            # Unmatched right char or mismatched chars.
            return False
    return not left_chars
