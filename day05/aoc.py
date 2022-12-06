from collections import defaultdict, deque

from parse import parse


def crates_in_stacks(s: str) -> dict:
    return {1 + int(((i + 1) / 4)): s[i + 1] for i in range(len(s)) if s.startswith("[", i)}


class Stack:
    def __init__(self):
        self.crates = deque()

    def pop(self) -> list:
        return self.crates.pop()

    def push(self, crate):
        self.crates.appendleft(crate)

    def __repr__(self) -> str:
        return ",".join(self.crates)


class Order:
    def __init__(self, txt: str):
        parsed = parse("move {crates:d} from {source:d} to {target:d}", txt)
        self.__dict__ = self.__dict__ | parsed.named

    def __repr__(self) -> str:
        return f"move {self.crates} from {self.source} to {self.target}"


def build_stacks(stack_lines: list[str]):
    lines = deque()
    for line in stack_lines:
        lines.appendleft(line)
    stacks = defaultdict(Stack)
    while lines:
        line = lines.pop()
        crate_assignments = crates_in_stacks(line)
        for stack, crate in crate_assignments.items():
            stacks[stack].push(crate)
    return stacks


def parse_input(lines):
    stack_line_count = 0
    for line in lines:
        stack_line_count += 1
        if line.strip().startswith("1"):
            break
    stacks = build_stacks(lines[: stack_line_count - 1])
    order_lines = lines[stack_line_count + 1 :]
    orders = [Order(line.strip()) for line in order_lines]
    return stacks, orders


def part1(data):
    """Solve part 1."""
    stacks, orders = data
    for order in orders:
        # print(order)
        for _ in range(order.crates):
            source = stacks[order.source]
            target = stacks[order.target]
            # print(source, ">", target)
            target.crates.append(source.pop())
            # print(source, "|", target)

    # for i in range(len(stacks)):
    #     print(i + 1, stacks[i + 1])

    return "".join(stacks[i].crates[-1] for i in range(1, len(stacks) + 1))


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = open("input.txt").readlines()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
