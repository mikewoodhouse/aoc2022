import pathlib

# from dataclasses import dataclass


def parse_input(puzzle_input):
    return puzzle_input


def part1(data: list[str]):
    xreg = 1
    cycle = 0
    cycles_until_done = 0
    value = 0
    program = iter(data)
    accum = 0
    running = True
    while running:
        cycle += 1
        if cycles_until_done == 0:
            try:
                line = next(program)
                # print(line)
            except StopIteration:
                running = False
            xreg += value
            # print(f"{cycle=} {line=} {xreg=} {cycles_until_done=}")

            if line.startswith("noop"):
                value = 0
            else:
                value = int(line.split(" ")[1])
                cycles_until_done = 1
        else:
            # print("not done")
            cycles_until_done -= 1

        if (cycle - 20) % 40 == 0:
            # print(f"{cycle=} {xreg=}")
            accum += xreg * cycle

    return accum


class Display:
    def __init__(self):
        self.s = ["." for _ in range(240)]

    def set(self, idx, what):
        self.s[idx - 1] = what

    def show(self):
        for i in range(0, 240, 40):
            print("".join(self.s[i : i + 40]))


def part2(data):
    sprite = "###" + "." * 37
    display = Display()
    display.show()
    row = 0
    xreg = 1
    pixel = 0
    cycles_until_done = 0
    value = 0
    program = iter(data)
    running = True
    while running:
        print(f"set({pixel=}, {xreg=}, {sprite[xreg]=}")
        display.set(row * 40 + pixel, sprite[xreg])

        pixel += 1
        if cycles_until_done == 0:
            try:
                line = next(program)
                # print(line)
            except StopIteration:
                running = False
            xreg += value
            sprite = "." * (xreg - 1) + "###" + "." * (40 - xreg - 2)
            print(xreg, sprite)
            # print(f"{cycle=} {line=} {xreg=} {cycles_until_done=}")

            if line.startswith("noop"):
                value = 0
            else:
                value = int(line.split(" ")[1])
                cycles_until_done = 1
        else:
            # print("not done")
            cycles_until_done -= 1
        if pixel > 39:
            row += 1
            pixel = 0
    display.show()


def solve(puzzle_input):
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("example.txt").read_text().strip().split("\n")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
