# LC 471. Encode String with Shortest Length

'''
Given a string s, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. k should be a positive integer.

If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.

Example 1:

Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.

Example 2:

Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
'''

class Solution:
    @lru_cache(None)
    def encode(self, s: str) -> str:
        encode = s
        i = (s + s).find(s, 1)

        if i < len(s):
            encode = str(len(s) // i) + "[" + self.encode(s[:i]) + "]"

        for i in range(1, len(s)):
            multi = self.encode(s[:i]) + self.encode(s[i:])

            if len(multi) < len(encode):
                encode = multi

        return encode

"""
Note:
- Finding repeated pattern technique
    - Concatenate string into two and remove first and last letter
    - If original string exist in the concatenated string, repeat exist
    - The index of beginning equals the length of the pattern
    - Proof:
        - Let's say there is a 4 repeat pattern "A+B+C+D"
        - If ABCD exist in BCDABC, then there exist a point idx (in this case B)
          where A=B, B=C, C=D, D=E. Therefore, A=B=C=D, and idx==len(A)
"""
