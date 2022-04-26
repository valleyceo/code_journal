# Transpose trick in Python
def transpose(M: List[List[int]]) -> List[List[int]]:
    return [list(i) for i in zip(*M)]

# Shorter using map
def transpose(M: List[List[int]]) -> List[List[int]]:
    return map(list, zip(*M))
