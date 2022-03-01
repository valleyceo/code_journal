# Find the Smallest Subarray Coverin All Values

'''
- Given array of strings and a set of strings
- Return the indices of starting and ending index of a shortest subarray that contains all strings in the set
'''

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

# O(n) time | O(m) space


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        while remaining_to_cover == 0:
            if result == Subarray(
                    start=-1,
                    end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result


'''
1. Create hashtable of the keywords (with counter)
2. For every word iteration, if it exist in the keyword
3. If counter is zero, move the left idx and add the next keyword
4. Repeat from 2
'''
