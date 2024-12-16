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


def solve(input_lines: list[str], lowest_score: int = 103512):
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

    frontier: list[
        tuple[int, tuple[complex, complex], frozenset[tuple[complex, complex]]]
    ] = [(0, (start, 1 + 0j), frozenset({(start, 1 + 0j)}))]

    visited: dict[
        tuple[complex, complex], tuple[int, set[frozenset[tuple[complex, complex]]]]
    ] = {}

    best_paths: list[frozenset[tuple[complex, complex]]] = []

    while frontier:
        score, (p, d), path = frontier.pop(0)
        if p == end:
            best_paths.append(path)
            continue

        if (p, d) in visited:
            _score, paths = visited[(p, d)]
            assert _score <= score
            if _score == score:
                visited[(p, d)] = (score, paths | {path})
            continue
        else:
            visited[(p, d)] = (score, {path})

        if (
            (next_pos := p + d) in world
            and next_pos not in path
            and score + 1 <= lowest_score
        ):
            bisect.insort(
                frontier,
                (score + 1, (next_pos, d), path | {(next_pos, d)}),
                key=lambda x: x[0],
            )

        if (
            (left_space := p + d * 1j) in world
            and left_space not in path
            and score + 1001 <= lowest_score
        ):
            bisect.insort(
                frontier,
                (score + 1001, (left_space, d * 1j), path | {(left_space, d * 1j)}),
                key=lambda x: x[0],
            )

        if (
            (right_space := p + d * -1j) in world
            and right_space not in path
            and score + 1001 <= lowest_score
        ):
            bisect.insort(
                frontier,
                (score + 1001, (right_space, d * -1j), path | {(right_space, d * -1j)}),
                key=lambda x: x[0],
            )

    n = 0
    all_visited: set[tuple[complex, complex]] = {p for path in best_paths for p in path}

    while len(all_visited) != n:
        n = len(all_visited)
        for p in all_visited:
            _, paths = visited.get(p, (0, set()))
            for path in paths:
                all_visited = all_visited | path

    return len(set(p for p, _ in all_visited))


def main():
    with open("16/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print()
    print(solve(test_input))


if __name__ == "__main__":
    main()
