def is_mas(c: list[str], key: str = "MAS"):
    return ''.join(c) == key or ''.join(c[::-1]) == key


def solve(input_lines: list[str]):
    total = 0

    for x in range(1, len(input_lines) - 1):
        for y in range(1, len(input_lines[x]) - 1):
            x1 = [input_lines[x + i][y + i] for i in range(-1, 2)]
            x2 = [input_lines[x - i][y + i] for i in range(-1, 2)]
            if is_mas(x1) and is_mas(x2):
                total += 1

    return total


def main():
    with open("04/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
