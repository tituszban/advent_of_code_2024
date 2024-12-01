from collections import defaultdict


def solve(input_lines: list[str]):
    split_ids = [list(map(int, line.split())) for line in input_lines]
    a, b = [[n[i] for n in split_ids] for i in [0, 1]]
    b_count = defaultdict(int)
    for m in b:
        b_count[m] += 1

    return sum(n * b_count[n] for n in a)


def main():
    with open("01/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
