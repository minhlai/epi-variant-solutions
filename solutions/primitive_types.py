# Write expressions that use bitwise operators, equalty checks, and Boolean operators to do the following in O(1) time.

# Right propagate the rightmost ste bit in x
def right_propagate(x):
    return x - 1 | x

# Compute x mod a power of two
def mod_two(x, y):
    return y - 1 & x

# Test if x is a power of 2
def is_pow_two(x):
    x &= x - 1
    return x == 0

# swap bits
def swap_bits(x, a, b):
    # get value of bits at positions a and b
    a_bit = x >> a & 1
    b_bit = x >> b & 1
    # set bit at position a to b_bit and visa versa
    x ^= (-a_bit ^ x) & (1 << b)
    x ^= (-b_bit ^ x) & (1 << a)
    return x