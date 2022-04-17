# LC 467. Unique Substrings in Wraparound String

'''
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

Example 1:

Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.

Example 2:

Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.

Example 3:

Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
'''
# O(n) time | O(n) space
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        counter = {c: 1 for c in p}
        count = 1

        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:
                count += 1
            else:
                count = 1

            counter[p[i]] = max(counter[p[i]], count)
        return sum(counter.values())

"""
NOTE:
- Longest substring startin "a"(ex: "abcde") includes all smaller substring ("ab", "abc")
- Thus, you only need to know the longest substring of all starting char. (store max in hash map)
- Same can be said to ending char which is easier to use on interation. "abcde" includes "bcde", "cde"
"""
