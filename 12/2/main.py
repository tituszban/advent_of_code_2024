from collections import defaultdict
from itertools import groupby


def find_edges(perimiter: list[complex], transpose: bool = False):
    if transpose:
        perimiter = [p.imag + p.real * 1j for p in perimiter]
    by_imag = {
        k: [int(v.real) for v in g]
        for k, g in groupby(
            sorted(perimiter, key=lambda p: p.imag), 
            lambda p: int(p.imag)
        )
    }

    edges = 0
    for v in by_imag.values():
        s = sorted(v)
        edges += 1
        for i, j in zip(s, s[1:]):
            if j - i > 1:
                edges += 1

    return edges


def solve(input_lines: list[str]):
    garden = {
        x + y * 1j: c for y, line in enumerate(input_lines) for x, c in enumerate(line)
    }
    cost = 0
    while garden:
        seen: set[complex] = set()
        start, c = list(garden.items())[0]
        queue = [start]
        perimiter: dict[complex, list[complex]] = defaultdict(list)
        
        while queue:
            current = queue.pop()
            if current in seen:
                continue
            seen.add(current)
            for d in [1 + 0j, -1 + 0j, 1j, -1j]:
                if (p := garden.get(current + d)) and p == c:
                    queue.append(current + d)
                else:
                    perimiter[d].append(current)

        edges = sum(find_edges(v, k.imag == 0) for k, v in perimiter.items())
        cost += len(seen) * edges
        for s in seen:
            del garden[s]
    return cost


def main():
    with open("12/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
