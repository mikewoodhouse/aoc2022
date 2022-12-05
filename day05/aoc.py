import pathlib

from parse import parse


class Stack:
    def __init__(self):
        self.creates = []

    def pop(self, how_many) -> list:
        pass


class Order:
    def __init__(self, txt: str):
        parsed = parse("move {crates:d} from {source:d} to {target:d}", txt)
        print(parsed.named)
        self.__dict__ = self.__dict__ | parsed.named


def build_stacks(stack_lines):
    pass


def parse_input(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split("\n")
    stack_line_count = 0
    for line in lines:
        if not line:
            stack_line_count += 1
            break
    stacks = build_stacks(lines[stack_line_count:])
    orders = [Order(line) for line in lines[:stack_line_count]]
    return stacks, orders


def part1(data):
    """Solve part 1."""


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("input.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
