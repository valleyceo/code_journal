# Knapsack

'''
- Given a set of items with value and weight
- Select the maximum value that satisfies the weight constraint
'''
# O(nw) time | O(nw) space
Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:

    # Returns the optimum value when we choose from items[:k + 1] and have a
    # capacity of available_capacity.
    @functools.lru_cache(None)
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            # No items can be chosen.
            return 0

        without_curr_item = optimum_subject_to_item_and_capacity(
            k - 1, available_capacity)
        with_curr_item = (0 if available_capacity < items[k].weight else
                          (items[k].value +
                           optimum_subject_to_item_and_capacity(
                               k - 1, available_capacity - items[k].weight)))
        return max(without_curr_item, with_curr_item)

    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


'''
- Example:
ID Value Weight:
a 60 5
b 50 3
c 70 4
d 30 2

- Table:
idx -> 0 1 2  3  4  5
a   -> 0 0 0  0  0  60
ab  -> 0 0 0  50 50 60
abc -> 0 0 0  50 70 70
abcd-> 0 0 30 50 70 80
'''
