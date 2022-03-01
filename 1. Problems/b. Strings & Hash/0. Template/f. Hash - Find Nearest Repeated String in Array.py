# Find the Nearest Repeated Entires in an Array

'''
- Given an array of strings
- Find the closest two pair of strings that are the same
'''

# O(n) time | O(d) space, d is the number of distinct strings in array
def find_nearest_repetition(paragraph: List[str]) -> int:

    word_to_latest_index: Dict[str, int] = {}
    nearest_repeated_distance = float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - latest_equal_word)
        word_to_latest_index[word] = i
    return typing.cast(int, nearest_repeated_distance
                       ) if nearest_repeated_distance != float('inf') else -1
