# Count the Number of Score Combinations

'''
- Given a final score and scores of individual plays
- Return number of combinations of plays that result in final score

- Example: American football (2,3,7 possible points) with final score of 12
- Solution: {6x2}, {2x3+3x2}, {2x1 + 3x1 + 7x1}, {3x4}
'''
# O(sn) time, s is possible scores | O(sn) space
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:

    # One way to reach 0.
    num_combinations_for_score = [[1] + [0] * final_score
                                  for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[i - 1][j]
                                 if i >= 1 else 0)
            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]]
                if j >= individual_play_scores[i] else 0)
            num_combinations_for_score[i][j] = (without_this_play +
                                                with_this_play)
    return num_combinations_for_score[-1][-1]

'''
- DP table:

idx  -> 0 1 2 3 4 5 6 7 8 9 10 11 12
2    -> 1 0 1 0 1 0 1 0 1 0 1  0  1
2,3  -> 1 0 1 1 1 1 2 1 2 2 2  2  3
2,3,7-> 1 0 1 1 1 1 2 2 2 3 3  3  4
'''
