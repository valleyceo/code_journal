# Compute All String Decompositions

'''
- Given a input string and array of strings
- Return the starting indices of substrings of the sentence
'''

# O(N*n*m) time, N is length of sentence, m is number of words, n is length of each word
def find_all_substrings(s: str, words: List[str]) -> List[int]:
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                # curr_word occurs too many times for a match to be possible.
                return False
        return True

    word_to_freq = collections.Counter(words)
    unit_size = len(words[0])
    return [
        i for i in range(len(s) - unit_size * len(words) + 1)
        if match_all_words_in_dict(i)
    ]
