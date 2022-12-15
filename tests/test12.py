from aoc.aoc12 import Aoc, Grid


def test_grid():
    g = Grid(["abc", "def", "ghi"])
    assert g[1, 1] == ord("e") - 96
    g[2, 2] = "."
    assert g[2, 2] == "."


def test_grid_valid_moves():
    g = Grid(["abc", "dEf", "ghi"])
    vm = g.valid_moves(0, 0)
    assert len(vm) == 2


def test_highest():
    g = Grid(["abc", "dEf", "ghi"])
    n = g.top_cell()
    assert n.row == 1
    assert n.col == 1
