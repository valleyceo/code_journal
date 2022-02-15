# Multiplication

def multiply(x: int, y: int) -> int:

    running_sum = 0

    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1

    return running_sum
