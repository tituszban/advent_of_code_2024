from collections import defaultdict


def get_path(world: set[complex], start: complex, end: complex) -> tuple[complex, ...] | None:
    queue: list[tuple[complex, tuple[complex, ...]]] = [(start, (start,))]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction in [1 + 0j, -1 + 0j, 1j, -1j]:
            if current + direction in world:
                queue.append((current + direction, (*path, current + direction)))
    return None


def solve(input_lines: list[str], n: int = 100):
    world = {
        x + y * 1j
        for y, line in enumerate(input_lines)
        for x, c in enumerate(line)
        if c != "#"
    }
    start = next(
        (
            x + y * 1j
            for y, line in enumerate(input_lines)
            for x, c in enumerate(line)
            if c == "S"
        )
    )
    end = next(
        (
            x + y * 1j
            for y, line in enumerate(input_lines)
            for x, c in enumerate(line)
            if c == "E"
        )
    )

    path = {p: i for i, p in enumerate(get_path(world, start, end) or ())}

    cheats = defaultdict(int)
    for p1, v1 in path.items():
        for p2, v2 in path.items():
            d = int(abs(p1.real - p2.real) + abs(p1.imag - p2.imag))
            if d <= 20 and v2 - v1 - d >= n:
                cheats[v2 - v1 - d] += 1

    return sum(cheats.values())

    


def main():
    with open("20/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
