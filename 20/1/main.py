def get_path(world: set[complex], start: complex, end: complex) -> tuple[complex, ...]:
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
    return ()


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

    path = {p: i for i, p in enumerate(get_path(world, start, end))}

    cheats: list[tuple[complex, complex]] = []
    for s1 in [1 + 0j, -1 + 0j, 1j, -1j]:
        for s2 in [1 + 0j, -1 + 0j, 1j, -1j]:
            if s1 + s2 != 0:
                cheats.append((s1, s2))

    shortcuts = []
    for p, v in path.items():
        for cheat in cheats:
            s1, s2 = cheat
            if p + s1 not in path and (vc := path.get(p + s1 + s2)) is not None and vc - 2 > v:
                shortcuts.append((p, cheat, vc - v - 2))

    return len([v for _, _, v in shortcuts if v >= n])


def main():
    with open("20/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
