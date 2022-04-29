# LC 633. Sum of Square Numbers

'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return self.fermatTheorem(c)

    def naiveTLE(self, c: int) -> bool:
        for i in range(int(sqrt(c)+1)):
            for j in range(int(sqrt(c)+1)):
                if i*i + j*j == c:
                    return True

        return False

    # O(sqrt(c)log(c)) time | O(1) space
    def naiveOptimized(self, c: int) -> bool:
        for i in range(int(sqrt(c)+1)):
            j = sqrt(c - i * i)

            if int(j) == j:
                return True

        return False

    def fermatTheorem(self, c: int) -> bool:
        for i in range(2, int(sqrt(c)+1)):
            count = 0

            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i

                if i % 4 == 3 and count % 2:
                    return False

        return c % 4 != 3

"""
Fermat's Theorem:
    - Any positive number n is expressible as a sum of two squares if and only if the prime factorization of n, every prime of the form (4k + 3) occurs an even number of times
"""
