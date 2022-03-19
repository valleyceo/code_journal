# Find all divisors of a number

# O(n) time
def getDivisors(n):
    divs = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divs.append(i)

    return divs

# O(sqrt(n)) time
def getDivisors(n):
    divs = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n // i != i:
                divs.append(n//i)

            divs.append(i)

    return divs
