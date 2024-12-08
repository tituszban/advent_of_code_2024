from collections import defaultdict
from itertools import combinations


def solve(input_lines: list[str]):
    antenae: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for y, line in enumerate(input_lines):
        for x, char in enumerate(line):
            if char != ".":
                antenae[char].append((x, y))

    w, h = len(input_lines[0]), len(input_lines)

    def find_antinodes(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int] | None:
        x1, y1 = p1
        x2, y2 = p2

        dx, dy = x2 - x1, y2 - y1
        xn, yn = (x2 + dx, y2 + dy)
        if 0 <= xn < w and 0 <= yn < h:
            return xn, yn
        return None

    nodes: set[tuple[int, int]] = set()

    for positions in antenae.values():
        for p1, p2 in combinations(positions, 2):
            n1 = find_antinodes(p1, p2)
            if n1:
                nodes.add(n1)
            n2 = find_antinodes(p2, p1)
            if n2:
                nodes.add(n2)

    return len(nodes)


def main():
    with open("08/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
