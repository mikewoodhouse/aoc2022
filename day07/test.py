import aoc
import pytest

DAY = "06"


@pytest.fixture
def example():
    with open("example.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part1_example1(example):
    tree = aoc.build_tree(example)
    assert isinstance(tree, aoc.Dir)
    assert len(tree.children) == 2
    assert tree.filesize == 48381165
    a = tree.children["a"]
    e = a.children["e"]
    assert e.filesize == 584


@pytest.mark.skip()
def test_part2_example2(stream: str, expected: int):
    ...
