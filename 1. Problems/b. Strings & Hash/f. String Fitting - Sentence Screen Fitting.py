# LC 418. Sentence Screen Fitting

'''
Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.

Example 3:

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.
'''
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        s_len = len(s)
        s_idx = 0

        for _ in range(rows):
            s_idx += cols

            # If end of col is middle of word, find the last idx with space
            if s[s_idx % s_len] != ' ':
                while s_idx >= 0 and s[s_idx % s_len] != ' ':
                    s_idx -= 1

            # Move to the next starting character
            s_idx += 1

        return s_idx // s_len
