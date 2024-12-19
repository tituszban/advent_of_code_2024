from functools import cache

def solve(input_lines: list[str]):
    patterns = sorted(input_lines[0].split(", "), key=lambda x: len(x), reverse=False)
    targets = input_lines[2:]

    @cache
    def search(remaining_pattern: str):
        if remaining_pattern == "":
            return 1
        total = 0
        for pattern in patterns:
            if remaining_pattern.startswith(pattern):
                total += search(remaining_pattern[len(pattern):])
        return total
                
    matching_targets = [search(target) for target in targets]

    return sum(matching_targets)


def main():
    with open("19/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
