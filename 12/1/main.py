def solve(input_lines: list[str]):
    garden = {
        x + y * 1j: c for y, line in enumerate(input_lines) for x, c in enumerate(line)
    }
    cost = 0
    while garden:
        seen: set[complex] = set()
        start, c = list(garden.items())[0]
        queue = [start]
        perimiter = 0
        while queue:
            current = queue.pop()
            if current in seen:
                continue
            seen.add(current)
            for d in [1 + 0j, -1 + 0j, 1j, -1j]:
                if (p := garden.get(current + d)) and p == c:
                    queue.append(current + d)
                else:
                    perimiter += 1
        cost += perimiter * len(seen)
        for s in seen:
            del garden[s]
    return cost


def main():
    with open("12/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
