import pathlib
from dataclasses import dataclass

from parse import parse


@dataclass
class Move:
    move: str
    steps: int

    def __str__(self) -> str:
        return f"{self.move} {self.steps}"


def parse_line(line):
    res = parse("{move:S} {steps:d}", line.strip())
    return res.named


def parse_input(puzzle_input):

    moves = [Move(**parse_line(line)) for line in puzzle_input if line]

    print("U", sum(m.steps for m in moves if m.move == "U"))
    print("D", sum(m.steps for m in moves if m.move == "D"))
    print("L", sum(m.steps for m in moves if m.move == "L"))
    print("R", sum(m.steps for m in moves if m.move == "R"))

    return moves


MOVES = {
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

TAIL_MOVES = {
    (-2, -1): (-1, -1),
    (-2, 0): (-1, 0),
    (-2, 1): (-1, 1),
    (-1, -2): (-1, -1),
    (-1, -1): (0, 0),
    (-1, 0): (0, 0),
    (-1, 1): (0, 0),
    (-1, 2): (-1, 1),
    (0, -2): (0, -1),
    (0, -1): (0, 0),
    (0, 0): (0, 0),
    (0, 1): (0, 0),
    (0, 2): (0, 1),
    (1, -2): (1, -1),
    (1, -1): (0, 0),
    (1, 0): (0, 0),
    (1, 1): (0, 0),
    (1, 2): (1, 1),
    (2, -1): (1, -1),
    (2, 0): (1, 0),
    (2, 1): (1, 1),
}


def sign(x: int) -> int:
    return -1 if x < 0 else 1 if x > 0 else 0


def tail_vector(dx, dy) -> tuple:
    return (0, 0) if -2 < dx < 2 and -2 < dy < 2 else (sign(dx), sign(dy))


def move(from_pos, by):
    return (from_pos[0] + by[0], from_pos[1] + by[1])


def catch_up_to(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    # return move(tail, TAIL_MOVES[(dx, dy)])
    return move(tail, tail_vector(dx, dy))


def part1(data):
    h = (0, 0)
    t = (0, 0)
    visited = {t}
    for m in data:
        # print(m)
        for _ in range(m.steps):
            h = move(h, MOVES[m.move])
            t = catch_up_to(h, t)
            visited.add(t)
            # print(f"{h=}, {t=}, {len(visited)=}")
    return len(visited)


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("input.txt").read_text().strip().split("\n")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
