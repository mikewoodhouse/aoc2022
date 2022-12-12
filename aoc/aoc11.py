import math
import pathlib

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

    def inspect(self) -> None:
        def update(op, by, value) -> int:
            operand = value if by == "old" else int(by)
            if op == "*":
                return (value * operand) // 3
            elif op == "+":
                return (value + operand) // 3
            else:
                raise ValueError(f"unexpected operator: {op}")

        self.items = [update(self.operator, self.operand, item) for item in self.items]
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

    def solve(self, lines) -> int:
        monkeys = [Monkey(lines[i : i + 6]) for i in range(0, len(lines), 6)]
        for _ in range(20):
            for monkey in monkeys:
                monkey.inspect()
                for target, item in monkey.throwings():
                    monkeys[target].receive(item)
        top2 = sorted([m.inspect_count for m in monkeys], reverse=True)[:2]
        return math.prod(top2)

    def solution1(self):
        lines = self.input()
        return self.solve(lines)

    def solution2(self):
        return "Not yet"


if __name__ == "__main__":
    aoc = Aoc11()
    print(aoc.solve_example())
    print(aoc.solution1())
    print(aoc.solution2())
