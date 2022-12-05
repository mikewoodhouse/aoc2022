import aoc
import pytest
import pathlib

DAY = "05"


@pytest.fixture
def example():
    puzzle_input = pathlib.Path("example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly."""
    ...


@pytest.mark.skip()
def test_part1_example1(example):
    """Test part 1 on example input."""
    ...


@pytest.mark.skip()
def test_part2_example2(example):
    """Test part 2 on example input."""
    ...
