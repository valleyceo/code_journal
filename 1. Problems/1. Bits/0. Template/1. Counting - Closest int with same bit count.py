# Closest int with same bit counting

def closest_int_same_bit_count(x: int) -> int:

    num_unsigned_bits = 64

    for i in range(num_unsigned_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))
            return x

    raise ValueError('All bits are 0 or 1')
