# DP solution for catalan
def catalan(n):
    if (n == 0 or n == 1):
        return 1

    catalan = [0 for i in range(n + 1)]
    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j]
            catalan[i] *= catalan[i-j-1]

    # Return last entry
    return catalan[n]

# O(N) time, O(1) space
def catalan(n: int) -> int:
    C = 1

    for i in range(n):
        C = C * 2 * (2 * i + 1) / (i + 2)

    return int(C)
