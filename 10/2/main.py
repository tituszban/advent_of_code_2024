from collections import defaultdict


def solve(input_lines: list[str]):
    world = {
        (x + y * 1j): int(c)
        for y, line in enumerate(input_lines)
        for x, c in enumerate(line)
        if c != "."
    }
    f = 9
    frontier = {p: {(p,)} for p, n in world.items() if n == f}
    next_frontier: dict[complex, set[tuple[complex, ...]]] = defaultdict(set)

    while f > 0:
        f = f - 1
        for p, current in frontier.items():
            for offset in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j):
                pn = p + offset
                if (c := world.get(pn)) is None or c != f:
                    continue
                for head in current:
                    next_frontier[pn].add((*head, pn))
        frontier = next_frontier
        next_frontier = defaultdict(set)

    return sum(map(len, frontier.values()))


def main():
    with open("10/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
