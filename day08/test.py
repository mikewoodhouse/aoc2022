import pathlib

import aoc
import pytest


@pytest.fixture
def example():
    return aoc.parse_data(pathlib.Path("example.txt").read_text().split("\n"))


def test_part1_example1(example):
    print(example)
    assert aoc.visible_tree_count(example) == 21


@pytest.mark.skip()
def test_part2_example2(stream: str, expected: int):
    ...
