# Division

'''
Compute x // y

Get the largest k such that 2^k*y <= x, then subtract 2^k*y to x and
Note: This does not compute fractions
'''
def divide(x: int, y: int) -> int:

    result, power = 0, 32
    y_power = y << power

    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power

    return result

print(divide(17, 3))
