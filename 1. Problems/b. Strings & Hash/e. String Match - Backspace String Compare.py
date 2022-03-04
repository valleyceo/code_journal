# LC 844. Backspace String Compare

'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.iteratorSolution(S, T)

    # O(n) time | O(1) space
    def pointerSolution(self, S: str, T: str) -> bool:
        si = len(S) - 1
        ti = len(T) - 1
        sBackCt = 0
        tBackCt = 0

        while True:
            while si >= 0 and (sBackCt or S[si] == "#"):
                sBackCt += 1 if S[si] == "#" else -1
                si -= 1

            while ti >= 0 and (tBackCt or T[ti] == "#"):
                tBackCt += 1 if T[ti] == "#" else -1
                ti -= 1

            if not (si >= 0 and ti >= 0 and S[si] == T[ti]):
                return si == ti == -1

            si -= 1
            ti -= 1

    # O(n) time | O(1) space
    def iteratorSolution(self, S: str, T: str) -> bool:
        def func(string):
            backCt = 0

            for c in reversed(string):
                if c == "#":
                    backCt += 1
                elif backCt:
                    backCt -= 1
                else:
                    yield c

        return all(s == t for s, t in itertools.zip_longest(func(S), func(T)))

    # O(n) time | O(n) space
    def stackSolution(self, S: str, T: str) -> bool:
        s1 = []
        t1 = []

        for char in S:
            if char == '#':
                if s1:
                    s1.pop()
            else:
                s1.append(char)

        for char in T:
            if char == '#':
                if t1:
                    t1.pop()
            else:
                t1.append(char)

        return s1 == t1

    
