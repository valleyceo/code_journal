# LC 555. Split Concatenated Strings

'''
You are given an array of strings strs. You could concatenate these strings together into a loop, where for each string, you could choose to reverse it or not. Among all the possible loops

Return the lexicographically largest string after cutting the loop, which will make the looped string into a regular one.

Specifically, to find the lexicographically largest string, you need to experience two phases:

Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.
And your job is to find the lexicographically largest one among all the possible regular strings.

Example 1:

Input: strs = ["abc","xyz"]
Output: "zyxcba"
Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", where '-' represents the looped status.
The answer string came from the fourth looped one, where you could cut from the middle character 'a' and get "zyxcba".

Example 2:

Input: strs = ["abc"]
Output: "cba"
'''
# O(M*(M + N)) Time | O(M*N) Space
# M is length of list, N is avg length of each words
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [max(s, s[::-1]) for s in strs]
        res = ""

        for i in range(len(strs)):
            s = strs[i]
            s_rev = s[::-1]
            rest = "".join(strs[i+1:] + strs[:i])

            for k in range(len(s)):
                res = max(res, s[k:] + rest + s[:k])
                res = max(res, s_rev[k:] + rest + s_rev[:k])

        return res

"""
Note:
- Question:
    - String of words are connected in a loop, so word order cannot be changed
    - You can split this string-loop in any position and create a string
    - For each words, you can reverse it
    - Find the lexicographically largest string

- Insight:
    - Only 1 word can be split and placed in each end, the rest can simply be regular or reversed if that's larger
"""
