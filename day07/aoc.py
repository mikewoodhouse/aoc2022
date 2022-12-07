from __future__ import annotations

import pathlib

from parse import parse


class Dir:
    def __init__(self, parent: Dir = None, name: str = ""):
        self.parent = parent
        self.name = f"{self.parent.name}/{name}" if parent else "/"
        self.children = {}
        self.files = {}

    def up(self) -> Dir:
        return self.parent

    def switch_to(self, new_dir: str) -> Dir:
        return self.children[new_dir]

    def add_entry(self, entry: str):
        if not len(entry.strip()):
            return
        first, second = entry.split(" ")
        if first == "dir":
            if second not in self.children:
                self.children[second] = Dir(self, second)
        else:
            self.files[second] = int(first)

    @property
    def filesize(self) -> int:
        file_lengths = sum(self.files.values())
        child_sizes = sum(child.filesize for child in self.children.values())
        return child_sizes + file_lengths


def build_tree(data: list[str]) -> Dir:
    root = Dir()
    for line in data:
        if line.startswith("$"):
            if line == "$ cd /":
                current = root
            elif line == "$ cd ..":
                current = current.up()
            elif line != "$ ls":
                parsed = parse("$ cd {target_dir}", line)
                current = current.switch_to(parsed.named["target_dir"])
        else:
            current.add_entry(line)
    return root


def traverse(root, dirs):
    dirs.append(root)
    for child in root.children.values():
        traverse(child, dirs)


def solve_part1(data: list[str]):
    tree = build_tree(data)
    dirs = []
    traverse(tree, dirs)
    answer = sum(d.filesize for d in dirs if d.filesize <= 100_000)
    print(answer)


def solve_part2(data):
    tree = build_tree(data)
    dirs = []
    traverse(tree, dirs)
    available_space = 70_000_000 - tree.filesize
    additional_needed = 30_000_000 - available_space
    print(f"need another {additional_needed}")
    large_enough = filter(lambda d: d.filesize >= additional_needed, dirs)
    best = sorted(large_enough, key=lambda d: d.filesize)[0]
    print(best.filesize)


if __name__ == "__main__":
    data = pathlib.Path("input.txt").read_text().split("\n")
    solve_part1(data)
    solve_part2(data)
