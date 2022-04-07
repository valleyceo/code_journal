# LC 397. Integer Replacement

'''
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:

Input: n = 4
Output: 2
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0

        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n % 4 == 3 and n != 3:
                    n += 1
                else:
                    n -= 1

            count += 1

        return count


'''
NOTE:
- Dividing by two is simply shifting the bits by 1
- If remainder is 1, you have two options:
    - If last 2 bits are 01, removing it (00) is better than adding (10 -> same ones count)
    - If last 2 bits are 11, adding one is better (100 -> 1 less ones), unless 11 are the last remaining bits
'''
