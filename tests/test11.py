import pathlib

import pytest

from aoc.aoc11 import Aoc11, Monkey


@pytest.fixture
def example():
    dir = pathlib.Path(__file__).parent.parent / "example"
    path = dir / "example11.txt"
    return path.read_text().strip().split("\n")


def test_example_loads():
    aoc = Aoc11()
    ex = aoc.example()
    assert len(ex) > 0
    assert ex[0].startswith("Monkey")


def test_monkey_parse(example):
    m = Monkey(example[:6])
    assert m.id == 0
    assert m.items == [79, 98]
    assert m.operator == "*"
    assert m.operand == "19"
    assert m.divisor == 23
    assert m.if_true == 2
    assert m.if_false == 3


def test_monkey_inspect(example):
    m = Monkey(example[:6])
    m.inspect()
    assert m.items == [79 * 19 // 3, 98 * 19 // 3]


def test_monkey_throwings(example):
    m = Monkey(example[:6])
    m.inspect()
    throwings = list(m.throwings())
    assert throwings[0] == (3, 500)
    assert throwings[1] == (3, 620)
