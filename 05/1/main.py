from collections import defaultdict


def prepare_input(input_lines: list[str]):
    rules: dict[int, set[int]] = defaultdict(set)

    while input_lines[0] != "":
        line = input_lines.pop(0)
        a, b = line.split("|")
        rules[int(a)].add(int(b))
    input_lines.pop(0)

    pages: list[list[int]] = []
    while any(input_lines):
        pages.append(list(map(int, input_lines.pop(0).split(","))))

    return dict(rules), pages


def get_middle_if_valid(rules: dict[int, set[int]], page: list[int]):
    seen = set()
    middle = len(page) // 2
    middle_v = 0
    for i, n in enumerate(page):
        if i == middle:
            middle_v = n
        rule_set = rules.get(n, set())
        if rule_set.intersection(seen):
            return 0
        seen.add(n)
    return middle_v


def solve(input_lines: list[str]):
    rules, pages = prepare_input(input_lines)

    total = sum([get_middle_if_valid(rules, page) for page in pages])

    return total


def main():
    with open("05/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
