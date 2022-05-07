# LC 2262. Total Appeal of A String

'''
The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.
'''
# O(n) time | O(26) space
class Solution:
    def appealSum(self, s: str) -> int:
        return self.solution2(s)

    def solution1(self, s: str) -> int:
        last = {}
        res = 0

        for i, c in enumerate(s):
            last[c] = i + 1
            res += sum(last.values())

        return res

    """
    Intuition:
    - For each idx, you can count how many substring to the left contains letter x
    - Ex: abbc
             | at pos 3, {a:1, b:3, c:4}
        - abbc
        -  bbc
        -   bc
        -    c
        -> Counts a: 1, b: 3, c: 4
    """

    def solution2(self, s: str) -> int:
        n = len(s)
        last = defaultdict(lambda: -1)
        res = 0

        for i, c in enumerate(s):
            res += (i - last[c]) * (n - i)
            last[c] = i
        return res

    """
    Intuition:
    - For each char in pos, count substring that includes the char.
        - Multiply # from last occurence (left) # to end of string (right)
        - Why # to last occurence only and # to all the way right?
            - Ex: abbca
                    | at pos 2
                -   b
                -   bc
                -   bca
                -> 1 * 3 = 3
                *  bb  -> included in pos 1 iteration
                *  bbc -> included in pos 1 iteration
                * abb  -> included in pos 0 iteration
    """
