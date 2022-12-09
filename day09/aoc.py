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
    return [Move(**parse_line(line)) for line in puzzle_input if line]


MOVES = {
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0, 1),
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
    return move(tail, tail_vector(dx, dy))


def solve_for_rope(data, rope_len: int):
    rope = [(0, 0) for _ in range(rope_len)]
    visited = {rope[-1]}
    for m in data:
        for _ in range(m.steps):
            rope[0] = move(rope[0], MOVES[m.move])
            for k in range(1, len(rope)):
                rope[k] = catch_up_to(rope[k - 1], rope[k])
            visited.add(rope[-1])
    return len(visited)


def part1(data):
    return solve_for_rope(data, 2)


def part2(data):
    return solve_for_rope(data, 10)


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
