# Iterative Addition

def add(a, b):
    return a if b == 0 else add(a ^ b, (a & b) << 1)
