# Generate The Power Set

'''
- Given an input set
- Return its power set (all subsets including the input set)
- Example: {0,1,2} -> {null, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2}}
'''
# Time complexity: O(2^n)
# Space complexity: O(n * 2^n)
def generate_power_set(input_set: List[int]) -> List[List[int]]:

    # Generate all subsets whose intersection with input_set[0], ...,
    # input_set[to_be_selected - 1] is exactly selected_so_far.
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        # Generate all subsets that contain input_set[to_be_selected].
        directed_power_set(to_be_selected + 1,
                           selected_so_far + [input_set[to_be_selected]])

    power_set: List[List[int]] = []
    directed_power_set(0, [])
    return power_set


# Pythonic solution
def generate_power_set_pythonic(S):
    power_set = [[]]
    for a in S:
        power_set += [s + [a] for s in power_set]
    return power_set
