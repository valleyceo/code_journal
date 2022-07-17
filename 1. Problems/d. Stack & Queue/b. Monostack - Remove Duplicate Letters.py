# LC 316. Remove Duplicate Letters

'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return self.greedySolution(s)

    # O(N) time | O(N) space
    def greedySolution(self, s: str) -> str:
        count = Counter(s)
        pos = 0

        for i, c in enumerate(s):
            if c < s[pos]:
                pos = i

            count[c] -= 1

            if count[c] == 0:
                break

        return s[pos] + self.greedySolution(s[pos:].replace(s[pos], "")) if s else ""


    # O(N) time | O(N) space
    def monostackSolution(self, s: str) -> str:
        stack = []
        seen = set()

        last_occurence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurence[stack[-1]]:
                    val = stack.pop()
                    seen.discard(val)

                seen.add(c)
                stack.append(c)

        return "".join(stack)

"""
Note:
- Greedy solution intuition
    - Find the prefix which has duplicates: 'bac'dbac -> bac
    - Pick the smallest char (or the first char if unique): bac -> a
    - Place smallest char to front and recurse remaining string: 'a' + fnc(cdbac)

- Monostack solution intuition
    - Keep a monostack but pop only if there is a duplicate afterwards
    - You can keep last occurence map of each char to see if there exist a duplicate
"""
