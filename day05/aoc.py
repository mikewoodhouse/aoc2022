from collections import defaultdict, deque

from parse import parse


def crates_in_stacks(s: str) -> dict:
    return {1 + int(((i + 1) / 4)): s[i + 1] for i in range(len(s)) if s.startswith("[", i)}


class Stack:
    def __init__(self):
        self.crates = []

    def pop(self) -> list:
        return self.crates.pop()

    def push(self, crate):
        self.crates.insert(0, crate)

    def __repr__(self) -> str:
        return ",".join(self.crates)


class Order:
    def __init__(self, txt: str):
        parsed = parse("move {crates:d} from {source:d} to {target:d}", txt)
        self.__dict__ = self.__dict__ | parsed.named

    def __repr__(self) -> str:
        return f"move {self.crates} from {self.source} to {self.target}"


def print_stacks(stacks):
    for i in range(1, len(stacks) + 1):
        print(i, stacks[i])


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
    print_stacks(stacks)
    for order in orders:
        for _ in range(order.crates):
            source = stacks[order.source]
            target = stacks[order.target]
            target.crates.append(source.pop())

    return "".join(stacks[i].crates[-1] for i in range(1, len(stacks) + 1))


def part2(data):
    """Solve part 2."""
    stacks, orders = data
    for id in range(1, len(stacks) + 1):
        print(id, stacks[id])
    for order in orders:
        source = stacks[order.source]
        target = stacks[order.target]
        print(f"{order.source}: {source} -> {order.target}: {target}")
        print(f"source.crates[-{order.crates} :] = {source.crates[:order.crates]}")
        crates_to_move = [source.pop() for _ in order.crates]
        target.crates.extend(crates_to_move)
        print(f"{order.source}: {source} && {order.target}: {target}")

    return "".join(stacks[i].crates[-1] for i in range(1, len(stacks) + 1))


def solve(puzzle_input):

    data = parse_input(puzzle_input)
    solution1 = part1(data)
    print(solution1)

    # data = parse_input(puzzle_input)
    # solution2 = part2(data)
    # print(solution2)


if __name__ == "__main__":
    puzzle_input = open("input.txt").readlines()
    solve(puzzle_input)
