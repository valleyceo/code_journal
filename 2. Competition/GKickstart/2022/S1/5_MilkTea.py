"""Starter Code for Milk Tea CC Problem"""
from itertools import permutations
import sys

def getComplaints(next_best, dp, people):
    complaints = 0

    for i, c in enumerate(dp):
        if next_best[i] == 0:
            complaints += c
        else:
            complaints += people - c

    return complaints

# Complete the count_complaints function
def count_complaints(preferences, forbiddens, n):
    dp = [0] * n

    for p in preferences:
        for i, c in enumerate(p):
            dp[i] += int(c)

    # best setting
    best = [0] * n
    for i, c in enumerate(dp):
        if c >= n//2:
            best[i] = 1

    fset = set()
    for f in forbiddens:
        fset.add(tuple(map(int, f)))

    minComplaints = sys.maxsize
    for i in range(n + 1):
        ones = [1] * i
        zeros = [0] * (n - i)
        arr = ones + zeros

        for mask in set(permutations(arr, n)):
            next_best = best.copy()

            for i in range(n):
                if mask[i]:
                    next_best[i] ^= 1

            if tuple(next_best) not in fset:
                minComplaints = min(minComplaints, getComplaints(next_best, dp, len(preferences)))

        if minComplaints != sys.maxsize:
            break

    return minComplaints

if __name__ == '__main__':
    # Read number of test cases
    num_cases = int(input())

    for tc in range(1, num_cases + 1):
        # Read number of friends, number of forbidden teas, and number of options
        num_friends, num_forbidden, num_options = map(int, input().split())

        # Read the friends' preferences
        preferences = [input() for _ in range(num_friends)]

        # Read the forbidden teas
        forbiddens = [input() for _ in range(num_forbidden)]

        print("Case #%d: %d" % (tc, count_complaints(preferences, forbiddens, num_options)))
