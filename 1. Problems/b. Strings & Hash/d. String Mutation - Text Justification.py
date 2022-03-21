# 68. Text Justification

'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        word_count = 0
        curr_len = 0
        curr_words = []

        for word in words:
            if curr_len + len(word) + word_count > maxWidth:
                space_len = maxWidth - curr_len
                res.append(self.createSentence(curr_words, space_len))

                word_count = 1
                curr_len = len(word)
                curr_words = [word]
            else:
                word_count += 1
                curr_len += len(word)
                curr_words.append(word)

        last_sentence = curr_words[0]

        for word in curr_words[1:]:
            last_sentence += " " + word

        space_len = maxWidth - len(last_sentence)

        res.append(last_sentence + " " * space_len)
        return res

    def createSentence(self, curr_words, space_len):
        if len(curr_words) == 1:
            return curr_words[0] + " " * space_len

        min_space = space_len // (len(curr_words) - 1)
        extra_space = space_len % (len(curr_words) - 1)
        res = curr_words[0]

        for i in range(1, len(curr_words)):

            spaces = min_space

            if extra_space > 0:
                spaces += 1
                extra_space -= 1

            res += " " * spaces + curr_words[i]

        return res
