import pytest
from main_calc.main import ClassJustForTesting


def test_one():
    instance = ClassJustForTesting()
    assert instance.variable_value == 10
