import pathlib


class Packet:
    def __init__(self, stream: str):
        self.stream = stream

    def complete_index(self) -> int:
        for i in range(len(self.stream) - 4):
            s = set(self.stream[i : i + 4])
            if len(s) == 4:
                return i + 4

    def start_of_message(self) -> int:
        for i in range(len(self.stream) - 14):
            s = set(self.stream[i : i + 14])
            if len(s) == 14:
                return i + 14


def part1(data):
    return Packet(data).complete_index()


def part2(data):
    return Packet(data).start_of_message()


if __name__ == "__main__":
    data = pathlib.Path("input.txt").read_text()
    solution1 = part1(data)
    solution2 = part2(data)
    print(solution1, solution2)
