from operator import add, mul
from itertools import product


def find_operators(total: int, numbers: list[int]) -> bool:
    for operators in product([add, mul], repeat=len(numbers) - 1):
        result = numbers[0]
        for i, number in enumerate(numbers[1:]):
            result = operators[i](result, number)
        if result == total:
            return True
    return False


def solve(input_lines: list[str]):
    total = 0

    for line in input_lines:
        a, b = line.split(": ")
        numbers = list(map(int, b.split()))
        if find_operators(int(a), numbers):
            total += int(a)

    return total


def main():
    with open("07/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
