import pathlib

import pytest

import day03 as aoc


DAY = "03"

PUZZLE_DIR = pathlib.Path(__file__).parent

pytest


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / f"example{DAY}.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly."""
    assert len(example) == 6
    assert len(example[0]) == 24


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 157


def test_part2_example2(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 70
