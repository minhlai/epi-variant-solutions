from solutions.primitive_types import *

def test_right_propagate():
    assert right_propagate(int("01010000", 2)) == int("01011111", 2)

def test_mod_two():
    assert mod_two(77, 64) == 13

def test_is_pow_two():
    assert is_pow_two(1) == True
    assert is_pow_two(2) == True
    assert is_pow_two(4) == True
    assert is_pow_two(8) == True
    assert is_pow_two(3) == False
    assert is_pow_two(5) == False
    assert is_pow_two(6) == False

def test_swap_bits():
    assert swap_bits(73, 1, 6) == 11