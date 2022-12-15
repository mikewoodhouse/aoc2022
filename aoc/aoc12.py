from __future__ import annotations

import pathlib
from typing import Optional

from parse import search

"""
find E. Which is height "z" & add to tree
while S (0,0) not found:
    for each cell at current tree level:
        for each adjacent cell:
            if height is current or one lower
                add cell to tree at next level
            set current cell to "." (already visited)
"""


class Grid:
    def __init__(self, lines) -> None:
        self.cells = [[ord(c) - 96 for c in line] for line in lines]

    def __getitem__(self, rc: tuple) -> str:
        r, c = rc
        if 0 <= r < len(self.cells[0]) and 0 <= c < len(self.cells):
            return self.cells[r][c]
        return None

    def __setitem__(self, rc: tuple, value: str) -> str:
        r, c = rc
        self.cells[r][c] = value

    def valid_moves(self, r: int, c: int) -> list:
        def cell_at_offset(r, c, drdc) -> tuple:
            dr, dc = drdc
            return (r + dr, c + dc, self[r + dr, c + dc])

        return [cell_at_offset(r, c, rc) for rc in [(-1, 0), (1, 0), (0, -1), (0, 1)] if cell_at_offset(r, c, rc)[2]]

    def top_cell(self) -> Node:
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                if self[row, col] == ord("E") - 96:
                    self[row, col] = None
                    return Node(row, col, None, 26)


class Node:
    def __init__(self, row: int, col: int, parent: Optional[Node] = None, value: str = None) -> None:
        self.row, self.col = row, col
        self.value = value
        self.children = []
        self.length = parent.length + 1 if parent else 0

    def add_child(self, node: Node) -> None:
        self.children.append(node)

    def iterate_to_origin(self, grid: Grid) -> int:
        for child in self.children:
            vms = grid.valid_moves(child.r, child.c)
            for vm in vms:
                r, c, v = vm
                if child.value - 1 <= v <= child.value:
                    if r == 0 and c == 0:
                        return child.length + 1
                    new_child = Node(r, c, v)
                    child.add_child(new_child)
                    if res := new_child.iterate_to_origin(grid):
                        return res
            grid[child.r, child.c] = None


def lines(filename: str):
    day = search("aoc{day:d}.py", __file__).named["day"]
    path = pathlib.Path(__file__).parent.parent / filename / f"{filename}{day}.txt"
    return list(filter(lambda line: len(line.strip()) > 0, path.read_text().strip().split("\n")))


class Aoc:
    def __init__(self) -> None:
        pass

    def example(self) -> str:
        return lines("example")

    def input(self):
        return lines("input")

    def solve_example(self):
        print("solving example...")
        self.solve(self.example())

    def solve(self, lines) -> int:
        grid = Grid(lines)
        top = grid.top_cell()

        for node in top.children:
            vms = grid.valid_moves(node.r, node.c)
            for vm in vms:
                r, c, v = vm
                if node.value - 1 <= v <= node.value:
                    node.add_child(Node(r, c, v))
            grid[node.r, node.c] = None

    def solution1(self):
        lines = self.input()
        return self.solve(lines)

    def solution2(self):
        lines = self.input()
        return self.solve(lines)


if __name__ == "__main__":
    aoc = Aoc()
    print(aoc.solve_example())
    print(aoc.solution1())
    print(aoc.solution2())
