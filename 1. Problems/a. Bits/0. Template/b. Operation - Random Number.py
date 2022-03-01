# Generate Uniform Random Numbers

'''
Implement a random number generator that generates a random integer i (btw a - b inclusive), given a random number generator that produces zero or one with equal probability?

Note: zero_one_random() is the provided random number generator.

Hint: how would you mimic a 3-side coin with 2-side coin?
'''
def uniform_random(lower_bound: int, upper_bound: int) -> int:

    number_of_outcomes = upper_bound - lower_bound + 1

    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:

            result = (result << 1) | zero_one_random()
            i += 1

        if result < number_of_outcomes:
            break
    return result + lower_bound

'''
Note:
- This is equivalent to random int btw 0 - b-a (add a at end).
- Find the smallest number form of 2^i - 1 that is greater than b-a.
- Create until a number below b-a is made (all numbers will have equal chance).

Time complexity: O(log(b-a+1)), each try is O(1)
'''
