def count_xmas(line: str, key: str = "XMAS") -> int:
    return line.count(key)


def get_diagonals(input_lines: list[str]):
    h, w = len(input_lines), len(input_lines[0])

    def get_diag(diagonal: list[tuple[int, int]]) -> str:
        return ''.join([input_lines[i][j] for i, j in diagonal if 0 <= i < h and 0 <= j < w])

    for i in range(h):
        d1 = [(i + j, j) for j in range(w) if i + j < h]
        yield get_diag(d1)
    for i in range(h):
        d2 = [(i - j, j) for j in range(w) if i - j >= 0]
        yield get_diag(d2)

    for j in range(1, w):
        d3 = [(i, i + j) for i in range(h) if i + j < w]
        yield get_diag(d3)
    for i in range(1, h):
        d4 = [(i + j, w - 1 - j) for j in range(w)]
        yield get_diag(d4)


def solve(input_lines: list[str]):
    total = 0

    total += sum([count_xmas(line) for line in input_lines])
    total += sum([count_xmas(''.join(reversed(line))) for line in input_lines])
    total += sum([count_xmas(''.join(line)) for line in zip(*input_lines)])
    total += sum([count_xmas(''.join(reversed(line)))
                 for line in zip(*input_lines)])

    # Check diagonals
    total += sum(count_xmas(line) for line in get_diagonals(input_lines))
    total += sum(count_xmas(''.join(reversed(line)))
                 for line in get_diagonals(input_lines))

    return total


def main():
    with open("04/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
