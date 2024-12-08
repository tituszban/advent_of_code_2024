from collections import defaultdict
from itertools import combinations
from math import gcd


def solve(input_lines: list[str]):
    antenae: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for y, line in enumerate(input_lines):
        for x, char in enumerate(line):
            if char != ".":
                antenae[char].append((x, y))

    w, h = len(input_lines[0]), len(input_lines)

    def find_antinodes(p1: tuple[int, int], p2: tuple[int, int]):
        x1, y1 = p1
        x2, y2 = p2

        dx, dy = x2 - x1, y2 - y1
        n = gcd(dx, dy)
        i = 0
        while 0 <= (xn := x2 + dx // n * i) < w and 0 <= (yn := y2 + dy // n * i) < h:
            yield xn, yn
            i += 1

    nodes: set[tuple[int, int]] = set()

    for positions in antenae.values():
        for p1, p2 in combinations(positions, 2):
            for n in find_antinodes(p1, p2):
                nodes.add(n)
            for n in find_antinodes(p2, p1):
                nodes.add(n)

    return len(nodes)


def main():
    with open("08/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
