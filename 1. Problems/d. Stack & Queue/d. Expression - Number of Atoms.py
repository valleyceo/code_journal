# LC 726. Number of Atoms

'''
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
'''
# O(n) time | O(26) space
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [Counter()]
        i = 0

        while i < N:
            if formula[i] == "(":
                stack.append(Counter())
                i += 1

            elif formula[i] == ")":
                top = stack.pop()
                i += 1

                start = i

                while i < N and formula[i].isdigit():
                    i += 1

                mult = int(formula[start: i] or 1)

                for k, v in top.items():
                    stack[-1][k] += v * mult

            else:
                start = i
                i += 1

                while i < N and formula[i].islower():
                    i += 1

                name = formula[start:i]
                start = i

                while i < N and formula[i].isdigit():
                    i += 1

                mult = int(formula[start:i] or 1)
                stack[-1][name] += mult

        res = ""

        for name in sorted(stack[-1]):
            res += name + (str(stack[-1][name]) if stack[-1][name] > 1 else "")

        return res
