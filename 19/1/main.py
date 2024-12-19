from functools import cache

def solve(input_lines: list[str]):
    patterns = sorted(input_lines[0].split(", "), key=lambda x: len(x), reverse=False)
    targets = input_lines[2:]

    @cache
    def search(remaining_pattern: str):
        if remaining_pattern == "":
            return True
        for pattern in patterns:
            if remaining_pattern.startswith(pattern):
                if search(remaining_pattern[len(pattern):]):
                    return True
                
    matching_targets = [target for target in targets if search(target)]

    return len(matching_targets)


def main():
    with open("19/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
