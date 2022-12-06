import pathlib
from collections import defaultdict, deque

from parse import parse


def crates_in_stacks(s: str) -> dict:
    return {int(1 + (i - 1) / 4): s[i + 1] for i in range(len(s)) if s.startswith("[", i)}


class Stack:
    def __init__(self):
        self.crates = deque()

    def pop(self, how_many) -> list:
        return self.crates.pop()

    def push(self, crate):
        self.crates.appendleft(crate)


class Order:
    def __init__(self, txt: str):
        parsed = parse("move {crates:d} from {source:d} to {target:d}", txt)
        print(parsed.named)
        self.__dict__ = self.__dict__ | parsed.named


def build_stacks(stack_lines: list[str]):
    lines = deque()
    for line in stack_lines:
        if line.startswith("1"):
            break
        lines.appendleft(line)
    stacks = defaultdict(Stack)
    while lines:
        line = lines.pop()
        crate_assignments = crates_in_stacks(line)
        for stack, crate in crate_assignments.items():
            stacks[stack].push(crate)
    return stacks


def parse_input(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split("\n")
    stack_line_count = 0
    for line in lines:
        print(line)
        if not line:
            stack_line_count += 1
            break
    stacks = build_stacks(lines[:stack_line_count])
    orders = [Order(line) for line in lines[stack_line_count + 1 :]]
    return stacks, orders


def part1(data):
    """Solve part 1."""
    stacks, orders = data
    print(stacks)


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
