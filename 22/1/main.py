from functools import cache


@cache
def calc_next(n: int) -> int:
    x1 = ((n * 64) ^ n) % 16777216
    x2 = ((x1 // 32) ^ x1) % 16777216
    x3 = ((x2 * 2048) ^ x2) % 16777216
    return x3


def solve(input_lines: list[str], repeat: int = 2000) -> int:
    total = 0
    for secret in input_lines:
        n = 0
        s = int(secret)
        while n < repeat:
            s = calc_next(s)
            n += 1
        total += s
    return total


def main():
    with open("22/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
