import re


def solve(input_line: list[str]):
    r = re.compile(r"mul\((\d+),(\d+)\)")
    matches = [m for line in input_line for m in r.findall(line)]
    s = 0
    for m in matches:
        s += int(m[0]) * int(m[1])
    return s


def main():
    with open("03/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
