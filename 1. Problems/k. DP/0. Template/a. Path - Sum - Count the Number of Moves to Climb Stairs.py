# Count the Number of Moves to Climb Stairs

'''
- You are climbinb up n-stairs and can advance 1 to k steps at a time
- Compute the number of ways to get to the last step
'''

# O(kn) time | O(kn) space
def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    @functools.lru_cache(None)
    def compute_number_of_ways_to_h(h):
        if h <= 1:
            return 1

        return sum(
            compute_number_of_ways_to_h(h - i)
            for i in range(1,
                           min(maximum_step, h) + 1))

    return compute_number_of_ways_to_h(top)

'''
- Formula: F(n,k) = sum(F(n-i,k)), i=1,2,...,k
'''
