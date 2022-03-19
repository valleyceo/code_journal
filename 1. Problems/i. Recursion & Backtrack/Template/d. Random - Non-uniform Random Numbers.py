# Generate Non-uniform Random Numbers

'''
- given n numbers with probabilities p0, p1, ... pn-1 which sum up to 1
- generate random number values uniformly according to probability
'''
# O(n) time | O(n) space


def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:

    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]


'''
- Create accumulated version of probability array
- Get random number [0, 1]
- Find the idx of first upper bound of the number
'''
