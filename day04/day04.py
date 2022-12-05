import pathlib


DAY = "04"


class Elf:
    def __init__(self, sections):
        start, end = sections.split("-")
        self.sections = set(range(int(start), int(end) + 1))

    def __eq__(self, __o: object) -> bool:
        return self.sections == __o.sections


class Pair:
    def __init__(self, input):
        self.elfs = [Elf(sections) for sections in input.split(",")]

    def one_is_redundant(self) -> bool:
        a, b = self.elfs
        return not (
            a.sections.difference(b.sections) and b.sections.difference(a.sections)
        )

    def has_overlap(self) -> bool:
        a, b = self.elfs
        return a.sections.intersection(b.sections)


def parse(puzzle_input: str) -> list[Pair]:
    """Parse input."""
    return [Pair(line) for line in puzzle_input.split()]


def part1(data):
    """Solve part 1."""
    return sum(1 for p in data if p.one_is_redundant())


def part2(data):
    """Solve part 2."""
    return sum(1 for p in data if p.has_overlap())


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = f"input{DAY}.txt"
    print(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
