# LC 1737. Change Minimum Characters to Satisfy One of Three Conditions

'''
You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.
'''
# O(A+B) time | O(26) space
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m = len(a)
        n = len(b)
        count_a = Counter(ord(c) - ord('a') for c in a)
        count_b = Counter(ord(c) - ord('a') for c in b)
        res = m + n - max((count_a + count_b).values()) # Case 3

        for i in range(25):
            count_a[i + 1] += count_a[i]
            count_b[i + 1] += count_b[i]

            res = min(res, m - count_a[i] + count_b[i]) # Case 1
            res = min(res, n - count_b[i] + count_a[i]) # Case 2

        return res

"""
Insight:
- Create a prefix sum of 26 characters for A and B string
- For each character 0 - 25, you can find the number to delete below character or above character
    - below: count[i]
    - above: n - count[i]
    - Ex: for case 1, you can delete A above c (n - count_a[c]) and delete B below c (count_b[c])
- Iterate through all character and find the min number of deletion
"""
