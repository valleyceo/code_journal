# Find the Majority Element

'''
- Given a sequence of strings, where more than half the strings are repetitions of a single string
- Find the majority element
'''


# O(N) time
def majority_search(stream: Iterator[str]) -> str:

    candidate_count = 0
    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate

'''
- Justification: if m/n > 1/2, then m/(n-2) > 1/2 and (m-1)/(n-2)
- (Explanation) Majority of elements will stay 1/2 or above even if majority or non-majority element is added/discarded. As a result, the majority element will always be left at the end.
'''
