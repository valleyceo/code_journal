# The Pretty Printing Problem (need to review)

'''
- Given a set of words to create a paragraph and max line length
- Create a paragraph such that messiness is minimized
- Messiness is measured by sum of number of blanks squared at end of each line
'''
# O(nL) time | O(n) space
def minimum_messiness(words: List[str], line_length: int) -> int:

    num_remaining_blanks = line_length - len(words[0])
    # min_messiness[i] is the minimum messiness when placing words[0:i + 1].
    min_messiness = ([num_remaining_blanks**2] +
                     [typing.cast(int, float('inf'))] * (len(words) - 1))
    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks**2
        # Try adding words[i - 1], words[i - 2], ...
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                # Not enough space to add more words.
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            current_line_messiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i],
                                   first_j_messiness + current_line_messiness)
    return min_messiness[-1]
