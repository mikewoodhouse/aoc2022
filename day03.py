import pathlib


DAY = "03"


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def front_back(line):
    n = len(line) // 2
    return line[:n], line[n:]


def item_score(item):
    return ord(item) - ord("a") + 1 if "a" <= item <= "z" else ord(item) - ord("A") + 27


def priority(sack):
    front, back = front_back(sack)
    f, b = set(front), set(back)
    in_both = "".join(f.intersection(b))
    return item_score(in_both)


def part1(data):
    """Solve part 1."""
    return sum(priority(rucksack) for rucksack in data)


def part2(data):
    """Solve part 2."""
    groups = [data[i : i + 3] for i in range(0, len(data), 3)]
    total = 0
    for group in groups:
        sets = [set(sack) for sack in group]
        common_01 = sets[0].intersection(sets[1])
        common_012 = common_01.intersection(sets[2])
        total += item_score("".join(common_012))
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = f"input{DAY}.txt"
    print(f"using {path}")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
