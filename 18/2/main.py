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


def find_exit(world: set[complex], w: int, h: int):
    frontier: list[tuple[complex, list[complex]]] = [(0 + 0j, [(0 + 0j)])]
    visited: set[complex] = set()
    goal = (w - 1) + (h - 1) * 1j

    while frontier:
        pos, path = frontier.pop(0)
        if pos == goal:
            return path
        if pos in visited:
            continue
        visited.add(pos)
        for d in [1, -1, 1j, -1j]:
            if pos + d in world:
                bisect.insort(
                    frontier, (pos + d, path + [pos + d]), key=lambda x: len(x[1])
                )


def solve(input_lines: list[str], w: int = 71, h: int = 71, n: int = 1024):
    for i in range(n, len(input_lines)):
        occupied = set([tuple(map(int, pair.split(","))) for pair in input_lines[:i + 1]])
        world = {
            x + y * 1j for y in range(h) for x in range(w) if (x, y) not in occupied
        }
        if (path := find_exit(world, w, h)) is None:
            return input_lines[i]
        # print(input_lines[i])
        # draw(world, w, h, path)


def main():
    with open("18/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
