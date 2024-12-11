from functools import cache

@cache
def iterate_stone(n: int):
    if n == 0:
        return [1]
    if (le := len(s := str(n))) % 2 == 0:
        return list(map(int, [s[: le // 2], s[le // 2 :]]))
    return [n * 2024]


def solve(input_lines: str):
    stones = list(map(int, input_lines.split()))
    for _ in range(25):
        stones = [n for stone in stones for n in iterate_stone(stone)]
    return len(stones)


def main():
    with open("11/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))[0]

    print(solve(test_input))


if __name__ == "__main__":
    main()
