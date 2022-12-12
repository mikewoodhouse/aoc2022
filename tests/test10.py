import pathlib

import pytest

from aoc.aoc10 import parse_input


@pytest.fixture
def example():
    puzzle_input = pathlib.Path("example/example10.txt").read_text()
    return parse_input(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example is not None
