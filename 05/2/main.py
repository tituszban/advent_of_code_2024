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


def create_order(rules: dict[int, set[int]], all_values: set[int]):
    valid_rules = {k: v for k, v in rules.items() if k in all_values}

    def get_head():
        possible_values = set(all_values)
        for after in valid_rules.values():
            possible_values -= after
        assert len(possible_values) == 1
        head = possible_values.pop()
        if head in valid_rules:
            valid_rules.pop(head)
        all_values.remove(head)
        return head

    while any(all_values):
        yield get_head()


def solve(input_lines: list[str]):
    rules, pages = prepare_input(input_lines)
    total = 0

    for page in pages:
        absolute_order = list(create_order(rules, set(page)))
        if absolute_order == page:
            continue

        assert len(absolute_order) == len(page)
        total += absolute_order[len(page) // 2]

    return total


def main():
    with open("05/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
