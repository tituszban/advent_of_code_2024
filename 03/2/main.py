import re


def solve(input_line: list[str]):
    r = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    matches = [m for line in input_line for m in r.findall(line)]
    s = 0
    enabled = True
    for _, a, b, do, dont in matches:
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            s += int(a) * int(b)
    return s


def main():
    with open("03/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
