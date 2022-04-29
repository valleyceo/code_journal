# Factorial with mod

"""
Compute N! % p
"""

"""
Naive
"""
def modFact(n, p):
    if n >= p:
        return 0

    res = 1

    for i in range(2, n + 1):
        res = (res * i) % p

    return res

"""
Sieve of Erastothenes
"""
def largestPower(n, p):
    x = 0

    # Calculate x = n/p + n/(p^2) + n/(p^3) + ....
    while (n):
        n //= p
        x += n
        
    return x

# (x^y) % p
def power( x, y, p):
    res = 1 # Initialize result
    x = x % p # Update x if it is more than
              # or equal to p
    while (y > 0) :

        # If y is odd, multiply x with result
        if (y & 1) :
            res = (res * x) % p

        # y must be even now
        y = y >> 1 # y = y/2
        x = (x * x) % p

    return res

# Returns n! % p
def modFact( n, p) :

    if (n >= p) :
        return 0

    res = 1
    isPrime = [1] * (n + 1)
    i = 2

    while(i * i <= n):
        if (isPrime[i]):
            for j in range(2 * i, n, i) :
                isPrime[j] = 0
        i += 1

    for i in range(2, n):
        if (isPrime[i]) :

            # Find the largest power of prime 'i'
            # that divides n
            k = largestPower(n, i)

            # Multiply result with (i^k) % p
            res = (res * power(i, k, p)) % p

    return res
