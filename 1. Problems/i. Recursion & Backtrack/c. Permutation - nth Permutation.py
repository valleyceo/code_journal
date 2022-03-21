# LC 60. Permutation Sequence

'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

Example 3:

Input: n = 3, k = 1
Output: "123"
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.factorialNumberSystem(n, k)

    # O(n^2) time | O(n) space
    def factorialNumberSystem(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']

        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))

        k -= 1
        output = []

        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return "".join(output)

'''
Explanation:
- https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
'''
