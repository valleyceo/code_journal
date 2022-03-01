# Compute the Largest Rectangle Under the Skyline (need to review)


'''
- Given array representing heights of adjacent buildings of unit width
- Compute area of largest rectangle contained in the skyline
'''

# O(n) time | O(n) space
def calculate_largest_rectangle(heights: List[int]) -> int:

    pillar_indices: List[int] = []
    max_rectangle_area = 0
    # By appending [0] to heights, we can uniformly handle the computation for
    # rectangle area here.
    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)
    return max_rectangle_area
