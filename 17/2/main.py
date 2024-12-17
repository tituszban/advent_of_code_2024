def operations(a: int):
    # This is my unique input simplified to basic operations.
    # TL;DR: Fuck the general solution.
    result = ""
    while a != 0:
        b = a % 8
        bs = b ^ 0b111
        c = (a >> bs) % 8
        a = a // 8
        b = b ^ c
        result = str(b % 8) + result
    return result


def to_dec(b8: str):
    b8 = b8[::-1]
    n = 0
    for i in range(len(b8)):
        n += int(b8[i]) * (8**i)
    return n


def search(start: str, target: str):
    def _explore_depth(s: str, d: int):
        for i in range(8):
            c = s[:d] + str(i) + s[d + 1 :]
            result = operations(to_dec(c))
            if result[d] == target[d]:
                yield c

    frontier = [start]
    for i in range(1, 16):
        new_frontier = []
        for s in frontier:
            new_frontier.extend(_explore_depth(s, i))
        frontier = new_frontier
    return to_dec(frontier[0])


def solve(input_lines: list[str]):
    return search("7000000000000000", "0355147130577142")


def main():
    with open("17/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print()
    print(solve(test_input))


if __name__ == "__main__":
    main()
