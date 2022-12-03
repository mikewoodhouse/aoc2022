import pathlib

import sys

SCORES = {
    "AX": 3 + 1,
    "AY": 6 + 2,
    "AZ": 0 + 3,
    "BX": 0 + 1,
    "BY": 3 + 2,
    "BZ": 6 + 3,
    "CX": 6 + 1,
    "CY": 0 + 2,
    "CZ": 3 + 3,
}


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split("\n")
    return ["".join(line.split(" ")) for line in lines]


def part1(data):
    """Solve part 1."""
    return sum(SCORES[match] for match in data)


PART2_TARGETS = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"},
}


def part2(data):
    """Solve part 2.
    X: lose
    Y: draw
    Z: win
    """

    return sum(
        SCORES["".join([match[0], PART2_TARGETS[match[1]][match[0]]])] for match in data
    )


def solve(puzzle_input):

    """Solve the puzzle for the given input."""

    data = parse(puzzle_input)

    solution1 = part1(data)

    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":

    for path in sys.argv[1:]:

        print(f"{path}:")

        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)

        print("\n".join(str(solution) for solution in solutions))
