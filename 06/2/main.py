class Map:
    def __init__(self, lines: list[str]):
        self._lines = lines
        self._rows = {
            i: [j for j, c in enumerate(line) if c == "#"]
            for i, line in enumerate(lines)}
        self._cols = {
            j: [i for i, line in enumerate(lines) if line[j] == "#"]
            for j in range(len(lines[0]))}

    def _next_obstacle(self, v: int, line: list[int], rev: bool) -> int:
        if rev:
            return next((i for i in reversed(line) if i < v), None)
        return next((i for i in line if i > v), None)

    def next_obstacle(self, x: int, y: int, facing: str) -> tuple[int, int]:
        if facing == "^":
            yn = self._next_obstacle(y, self._cols[x], True)
            return [(x, ys) for ys in range(y, yn or 0, -1)], yn is None
        if facing == "v":
            yn = self._next_obstacle(y, self._cols[x], False)
            return [(x, ys) for ys in range(y, yn or len(self._lines), 1)], yn is None
        if facing == ">":
            xn = self._next_obstacle(x, self._rows[y], False)
            return [(xs, y) for xs in range(x, xn or len(self._lines[0]), 1)], xn is None
        if facing == "<":
            xn = self._next_obstacle(x, self._rows[y], True)
            return [(xs, y) for xs in range(x, xn or 0, -1)], xn is None
        raise ValueError(f"Unknown facing: {facing}")

    def with_obstacle(self, x: int, y: int) -> "Map":
        new_lines = [
            ["#" if i == y and j == x else c for j, c in enumerate(line)]
            for i, line in enumerate(self._lines)]
        return Map(new_lines)


def next_facing(facing: str) -> str:
    if facing == "^":
        return ">"
    if facing == ">":
        return "v"
    if facing == "v":
        return "<"
    if facing == "<":
        return "^"
    raise ValueError(f"Unknown facing: {facing}")


def solve(input_lines: list[str]):
    world = Map(input_lines)
    x, y = next((x, y) for y, line in enumerate(input_lines)
                for x, c in enumerate(line) if c in "^v<>")
    start_x, start_y = x, y
    facing = input_lines[y][x]
    visited: list[tuple[int, int]] = []

    while True:
        p, end = world.next_obstacle(x, y, facing)
        visited.extend(p)
        if end:
            break
        x, y = p[-1]
        facing = next_facing(facing)

    def is_looping(ox: int, oy: int):
        _world = world.with_obstacle(ox, oy)
        _visited: list[tuple[int, int, str]] = []
        x, y = start_x, start_y
        facing = input_lines[y][x]
        while True:
            p, end = _world.next_obstacle(x, y, facing)
            for x, y in p:
                if (x, y, facing) in _visited:
                    return True
                _visited.append((x, y, facing))
            if end:
                return False
            x, y = p[-1]
            facing = next_facing(facing)

    total = len(set((x, y) for x, y in visited if is_looping(x, y)))

    return total


def main():
    with open("06/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
