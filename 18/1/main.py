import bisect

def draw(world: set[complex], w: int, h: int, path: list[complex]):
    for y in range(h):
        for x in range(w):
            if x + y * 1j in path:
                print("O", end="")
            elif x + y * 1j in world:
                print(".", end="")
            else:
                print("#", end="")
        print()

def solve(input_lines: list[str], w: int = 71, h: int = 71, n: int = 1024):
    occupied = set([tuple(map(int, pair.split(","))) for pair in input_lines[:n]])
    world = {x + y * 1j for y in range(h) for x in range(w) if (x, y) not in occupied}

    frontier: list[tuple[complex, list[complex]]] = [(0 + 0j, [(0 + 0j)])]
    visited: set[complex] = set()
    goal = (w - 1) + (h - 1) * 1j

    draw(world, w, h, [])

    while frontier:
        pos, path = frontier.pop(0)
        if pos == goal:
            draw(world, w, h, path)
            return len(path) - 1
        if pos in visited:
            continue
        visited.add(pos)
        for d in [1, -1, 1j, -1j]:
            if pos + d in world:
                bisect.insort(
                    frontier, (pos + d, path + [pos + d]), key=lambda x: len(x[1])
                )


def main():
    with open("18/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
