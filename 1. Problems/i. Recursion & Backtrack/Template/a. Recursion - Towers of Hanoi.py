# Towers of Hanoi

'''
- Given a 3 peg and 6 rings (increasing order) on the first peg
- Move the rings to the second peg
- Other rules: cannot place a larger ring above smaller ring and can move only one ring at a time
'''
# O(N^2) time
NUM_PEGS = 3

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg,
                                  use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg,
                                      to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg,
                                      from_peg)

    # Initialize pegs.
    result: List[List[int]] = []
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result
