def solve(input_lines: list[str]):
    split_ids = [list(map(int, line.split())) for line in input_lines]
    a, b = [[n[i] for n in split_ids] for i in [0, 1]]
    return sum(abs(m - n) for m, n in zip(sorted(a), sorted(b)))


def main():
    with open("01/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
