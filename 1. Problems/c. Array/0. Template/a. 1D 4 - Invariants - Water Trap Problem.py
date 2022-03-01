# Compute The Maximum Water Trapped by Pair of Vertical Lines

'''
- Given an integer array
- Return the pair which traps the maximum amount of water
'''

# O(n) time | O(1) space
def get_max_trapped_water(heights: List[int]) -> int:

    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        else:  # heights[i] <= heights[j].
            i += 1
    return max_water
