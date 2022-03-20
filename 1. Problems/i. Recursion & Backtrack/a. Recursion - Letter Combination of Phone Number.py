# LC 17. Letter Combinations of a Phone Number

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''
# Time: O(4^n * n) - permutation takes O(4^n), base case takes O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def recursion(idx: int) :

            if idx == len(digits):
                res.append("".join(path))
                return

            for c in phone_map[digits[idx]]:
                path[idx] = c
                recursion(idx+1)

        if len(digits) == 0:
            return []

        path = ['0'] * len(digits)
        res = []
        phone_map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        recursion(0)

        return res
