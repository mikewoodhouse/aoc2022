import pathlib

import pytest

import day04 as aoc


DAY = "04"

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / f"example{DAY}.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.mark.parametrize(
    "pair,redundant",
    [
        ("5-7,7-9", False),
        ("7-7,7-9", True),
    ],
)
def test_pair_redundancy(pair, redundant):
    p = aoc.Pair(pair)
    assert p.one_is_redundant() == redundant


@pytest.mark.parametrize(
    "pair,overlaps",
    [
        ("5-7,7-9", True),
        ("4-6,7-9", False),
    ],
)
def test_pair_overlappery(pair, overlaps):
    p = aoc.Pair(pair)
    if overlaps:
        assert p.has_overlap()
    else:
        assert not p.has_overlap()


def test_parse_example1(example):
    """Test that input is parsed properly."""
    assert len(example) == 6


@pytest.mark.skip()
def test_part1_example1(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 157


@pytest.mark.skip()
def test_part2_example2(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 70
