# Compute a Gray Code (need to review)

'''
- Given a number n
- Return n-bit gray code

- Gray Code: Sequence array where each successive integers differ only by 1 binary (as well as the wrap around)
- Example(n=3): {000,100,101,111,110,010,011,001} -> {0,4,5,7,6,2,3,1} or {0,1,3,2,6,7,5,4}
'''

def gray_code(num_bits: int) -> List[int]:
    def directed_gray_code(history):
        def differs_by_one_bit(x, y):
            bit_difference = x ^ y
            return bit_difference and not (bit_difference &
                                           (bit_difference - 1))

        if len(result) == 1 << num_bits:
            # Check if the first and last codes differ by one bit.
            return differs_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]
            candidate_next_code = previous_code ^ (1 << i)
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                if directed_gray_code(history):
                    return True
                del result[-1]
                history.remove(candidate_next_code)
        return False

    result = [0]
    directed_gray_code(set([0]))
    return result


def differ_by_1_bit(a, b):
    x = a ^ b
    if x == 0:
        return False
    while x & 1 == 0:
        x >>= 1
    return x == 1
