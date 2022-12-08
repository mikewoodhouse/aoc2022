import pathlib


def strings_to_ints(string: str) -> list[int]:
    return [int(c) for c in string]


def parse_data(data: list[str]) -> list[list[int]]:
    return list(map(strings_to_ints, data))


def visible_tree_count(forest):
    counts = [[0 for _ in forest[0]] for _ in forest]
    for row, strip in enumerate(forest):
        highest = -1
        for col, tree in enumerate(strip):
            if tree > highest:
                highest = tree
                counts[row][col] += 1

        highest = -1
        for col in range(len(strip) - 1, 0, -1):
            tree = strip[col]
            if tree > highest:
                highest = tree
                counts[row][col] += 1

    for col in range(len(forest[0])):
        highest = -1
        for row in range(len(forest)):
            tree = forest[row][col]
            if tree > highest:
                highest = tree
                counts[row][col] += 1

        highest = -1
        for row in range(len(forest) - 1, 0, -1):
            tree = forest[row][col]
            if tree > highest:
                highest = tree
                counts[row][col] += 1

    return sum(sum(ct > 0 for ct in row) for row in counts)


def best_scenic_score(data) -> int:
    best_score = 0
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            n, e, s, w = 0, 0, 0, 0
            tree = data[row][col]
            # North
            for r in range(row - 1, -1, -1):
                n += 1
                if data[r][col] >= tree:
                    break
            # East
            for c in range(col + 1, len(data[row])):
                e += 1
                if data[row][c] >= tree:
                    break
            # South
            for r in range(row + 1, len(data)):
                s += 1
                if data[r][col] >= tree:
                    break

            # West
            for c in range(col - 1, -1, -1):
                w += 1
                if data[row][c] >= tree:
                    break

            score = n * e * s * w
            if best_score < score:
                best_score = score
    return best_score


def solve_part1(data: list[str]):
    print(visible_tree_count(data))


def solve_part2(data):
    print(best_scenic_score(data))


if __name__ == "__main__":
    d = pathlib.Path(__file__).parent
    f = d / pathlib.Path("input.txt")
    data = parse_data(f.read_text().strip().split("\n"))
    solve_part1(data)
    solve_part2(data)
