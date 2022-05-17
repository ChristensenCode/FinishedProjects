import pytest
from ..Problem_61 import is_tri, is_square, is_penta


def test_is_tri_pass():
    assert is_tri(8128)


def test_is_tri_fail():
    assert is_tri(1234) is False


def test_is_square_pass():
    assert is_square(8281)


def test_is_square_fail():
    assert is_square(1234) is False
