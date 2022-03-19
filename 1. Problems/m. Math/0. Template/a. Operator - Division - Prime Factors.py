# Find all Prime Factors

# O(log(n)) best, O(n) worst time | O(1) space
def primeFactors(n):
    i = 2
    pfs = []

    while n > 1:
        if n % i == 0:
            n //= i
            pfs.append(i)
        else:
            i += 1

    return pfs
