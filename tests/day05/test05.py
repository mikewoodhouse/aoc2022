import pathlib

import pytest

import day05.aoc as aoc


@pytest.fixture
def example():
    example_dir = pathlib.Path(__file__).parent
    puzzle_input = pathlib.Path(f"{example_dir}/example.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_order_build():
    o = aoc.Order("move 42 from 99 to 111")
    assert o.crates == 42
    assert o.source == 99
    assert o.target == 111


def test_parse_example1(example):
    """Test that input is parsed properly."""
    stacks, orders = example
    assert len(stacks) == 3
    assert len(orders) == 4


@pytest.mark.skip()
def test_part1_example1(example):
    """Test part 1 on example input."""
    ...


@pytest.mark.skip()
def test_part2_example2(example):
    """Test part 2 on example input."""
    ...
