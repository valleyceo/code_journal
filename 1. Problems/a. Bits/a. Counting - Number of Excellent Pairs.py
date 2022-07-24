# LC 2354. Number of Excellent Pairs

'''
You are given a 0-indexed positive integer array nums and a positive integer k.

A pair of numbers (num1, num2) is called excellent if the following conditions are satisfied:

Both the numbers num1 and num2 exist in the array nums.
The sum of the number of set bits in num1 OR num2 and num1 AND num2 is greater than or equal to k, where OR is the bitwise OR operation and AND is the bitwise AND operation.
Return the number of distinct excellent pairs.

Two pairs (a, b) and (c, d) are considered distinct if either a != c or b != d. For example, (1, 2) and (2, 1) are distinct.

Note that a pair (num1, num2) such that num1 == num2 can also be excellent if you have at least one occurrence of num1 in the array.
'''

# O(nlogn) time | O(n) space
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def countBit(x):
            count = 0

            while x:
                count += 1
                x &= (x-1)

            return count

        nums = set(nums)
        counter = defaultdict(int)

        for n in nums:
            counter[countBit(n)] += 1

        res = 0

        for n, v in counter.items():
            for n2, v2 in counter.items():
                if n + n2 >= k:
                    res += v * v2

        return res

"""
Insight:
- Inclusion-Exclusion principle:
    - bit_count(A & B) + bit_count(A | B) = bit_count(A) + bit_count(B)
"""
