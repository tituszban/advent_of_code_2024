import bisect


def print_world(world: set[complex], visited: frozenset[complex]):
    max_x, max_y = max([int(w.real) for w in world]), max([int(w.imag) for w in world])

    print()
    for y in range(0, max_y + 2):
        for x in range(0, max_x + 2):
            i = x + y * 1j
            if i in visited:
                print("O", end="")
            elif x + y * 1j in world:
                print(".", end="")
            else:
                print("#", end="")
        print()


def solve(input_lines: list[str]):
    world: set[complex] = set()
    start: complex = 0 + 0j
    end: complex = 0 + 0j

    for y, line in enumerate(input_lines):
        for x, c in enumerate(line):
            if c != "#":
                world.add(x + y * 1j)
            if c == "S":
                start = x + y * 1j
            if c == "E":
                end = x + y * 1j

    frontier: list[tuple[int, tuple[complex, complex], frozenset[complex]]] = [
        (0, (start, 1 + 0j), frozenset({start}))
    ]
    explored: set[complex] = set()

    while frontier:
        score, (p, d), visited = frontier.pop(0)
        if p == end:
            return score
        if p in explored:
            continue
        explored.add(p)

        if (next_pos := p + d) in world and next_pos not in visited:
            bisect.insort(
                frontier,
                (score + 1, (next_pos, d), visited | {next_pos}),
                key=lambda x: x[0],
            )

        if (left_space := p + d * 1j) in world and left_space not in visited:
            bisect.insort(
                frontier,
                (score + 1001, (left_space, d * 1j), visited | {left_space}),
                key=lambda x: x[0],
            )

        if (right_space := p + d * -1j) in world and right_space not in visited:
            bisect.insort(
                frontier,
                (score + 1001, (right_space, d * -1j), visited | {right_space}),
                key=lambda x: x[0],
            )


def main():
    with open("16/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
