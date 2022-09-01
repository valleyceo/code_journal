# LC 1153. String Transforms Into Another String

'''
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
'''

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        conversion_map = {}
        unique_chars = set()

        for c1, c2 in zip(str1, str2):
            if c1 in conversion_map:
                if conversion_map[c1] != c2:
                    return False
            else:
                conversion_map[c1] = c2
                unique_chars.add(c2)

        return len(unique_chars) < 26
