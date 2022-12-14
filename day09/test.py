import pathlib

import aoc
import pytest


@pytest.fixture
def example1():
    puzzle_input = pathlib.Path("example1.txt").read_text().strip().split("\n")
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = pathlib.Path("example2.txt").read_text().strip().split("\n")
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert len(example1) == 8
    assert isinstance(example1[0], aoc.Move)


def test_parse_line():
    m = aoc.parse_line("R 11")
    assert m["move"] == "R"
    assert m["steps"] == 11


@pytest.mark.parametrize(
    "t,t2",
    [
        ((-2, -1), (-1, 0)),
        ((-2, 0), (-1, 0)),
        ((-2, 1), (-1, 0)),
        ((-1, -2), (0, -1)),
        ((-1, -1), (-1, -1)),
        ((-1, 0), (-1, 0)),
        ((-1, 1), (-1, 1)),
        ((-1, 2), (0, 1)),
        ((0, -2), (0, -1)),
        ((0, -1), (0, -1)),
        ((0, 0), (0, 0)),
        ((0, 1), (0, 1)),
        ((0, 2), (0, 1)),
        ((1, -2), (0, -1)),
        ((1, -1), (1, -1)),
        ((1, 0), (1, 0)),
        ((1, 1), (1, 1)),
        ((1, 2), (0, 1)),
        ((2, -1), (1, 0)),
        ((2, 0), (1, 0)),
        ((2, 1), (1, 0)),
    ],
)
def test_catch_up(t, t2):
    h = (0, 0)
    d = (h[0] - t[0], h[1] - t[1])
    mv = aoc.tail_vector(*d)
    new_t = aoc.catch_up_to(h, t)
    assert new_t == t2, f"{d=} {t=}, expected {t2=} got {new_t} {mv=}"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 13


def test_part2_example1(example1):
    assert aoc.part2(example1) == 1


def test_part2_example2(example2):
    assert aoc.part2(example2) == 36
