import math
import pathlib
from datetime import datetime

from parse import findall, parse


class Monkey:
    def __init__(self, lines: list[str]) -> None:
        self.id = parse("Monkey {id:d}:", lines[0]).named["id"]
        self.items = [f["item"] for f in findall("{item:d}", lines[1])]
        op = parse("Operation: new = old {operator} {operand}", lines[2].strip())
        self.operator = op.named["operator"]
        self.operand = op.named["operand"]
        self.divisor = parse("Test: divisible by {divisor:d}", lines[3].strip()).named["divisor"]
        self.if_true = parse("If true: throw to monkey {target:d}", lines[4].strip()).named["target"]
        self.if_false = parse("If false: throw to monkey {target:d}", lines[5].strip()).named["target"]
        self.inspect_count = 0

    def inspect(self, divide_by: int = 3, modulo: int = 1) -> None:
        def update(op, by, value) -> int:
            operand = value if by == "old" else int(by)
            if op == "*":
                return (value * operand) // divide_by
            elif op == "+":
                return (value + operand) // divide_by
            else:
                raise ValueError(f"unexpected operator: {op}")

        self.items = [update(self.operator, self.operand, item) % modulo for item in self.items]
        self.inspect_count += len(self.items)

    def throwings(self) -> list:
        def throw_to(item: int) -> int:
            return self.if_true if item % self.divisor == 0 else self.if_false

        for item in self.items:
            yield throw_to(item), item

        self.items.clear()

    def receive(self, item: int):
        self.items.append(item)


class Aoc11:
    def __init__(self) -> None:
        self.day = 11

    def example(self) -> str:
        path = pathlib.Path(__file__).parent.parent / "example" / f"example{self.day}.txt"
        return list(filter(lambda line: len(line.strip()) > 0, path.read_text().strip().split("\n")))

    def input(self):
        path = pathlib.Path(__file__).parent.parent / "input" / f"input{self.day}.txt"
        return list(filter(lambda line: len(line.strip()) > 0, path.read_text().strip().split("\n")))

    def solve_example(self):
        print("solving example...")
        lines = self.example()
        return self.solve(lines)

    def solve(self, lines, divide_by: int = 3, times: int = 20) -> int:
        monkeys = [Monkey(lines[i : i + 6]) for i in range(0, len(lines), 6)]
        modulo = math.prod([m.divisor for m in monkeys])
        for i in range(times):
            for monkey in monkeys:
                monkey.inspect(divide_by, modulo)
                for target, item in monkey.throwings():
                    monkeys[target].receive(item)
            if i % 20 == 0:
                print(datetime.now(), i)
        top2 = sorted([m.inspect_count for m in monkeys], reverse=True)[:2]
        return math.prod(top2)

    def solution1(self):
        lines = self.input()
        return self.solve(lines)

    def solution2(self):
        lines = self.input()
        return self.solve(lines, 1, 10_000)


if __name__ == "__main__":
    aoc = Aoc11()
    print(aoc.solve_example())
    print(aoc.solution1())
    print(aoc.solution2())
