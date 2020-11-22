# Euclidean Algorithm for finding greatest common divisor
# Complexity: O(log(a + b))
def gcd(m, n):
    while n != 0:
        m, n = n, m%n
    return m