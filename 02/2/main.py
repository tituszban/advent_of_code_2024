def is_safe(line: list[int]):
    all_increasing = None
    for a, b in zip(line, line[1:]):
        d = a - b
        increasing = d <= 0
        if all_increasing is None:
            all_increasing = increasing
        if increasing != all_increasing:
            return False
        ad = abs(d)
        if ad < 1:
            return False
        if ad > 3:
            return False
    return True


def brute_force_alternate_reports(line: list[int]):
    for i in range(len(line)):
        yield [n for j, n in enumerate(line) if i != j]


def solve(input_lines: list[list[int]]):
    return len([
        line
        for line in input_lines
        if is_safe(line) or any([is_safe(alt) for alt in brute_force_alternate_reports(line)])])


def main():
    with open("02/input.txt") as f:
        test_input = list(map(lambda line: list(
            map(int, line.strip().split())), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
