from collections import deque


def parse_input(input_line: str):
    is_data = True
    idx = 0
    stack: deque[tuple[int | None, int]] = deque()
    for d in input_line:
        if is_data:
            stack.append((idx, int(d)))
            idx += 1
        else:
            stack.append((None, int(d)))
        is_data = not is_data

    return stack


def compact(stack: deque[tuple[int | None, int]]):
    compacted: list[tuple[int, int]] = []

    while stack:
        idx, count = stack.popleft()
        if idx is not None:
            compacted.append((idx, count))
        else:
            while count > 0:
                _idx, _count = stack.pop()
                if _idx is None:
                    continue
                if _count <= count:
                    compacted.append((_idx, _count))
                    count -= _count
                else:
                    compacted.append((_idx, count))
                    stack.append((_idx, _count - count))
                    count = 0
    return compacted


def checksum(compacted: list[tuple[int, int]]):
    i = 0
    total = 0
    for idx, count in compacted:
        for _ in range(count):
            total += idx * i
            i += 1
    return total


def solve(input_line: str):
    stack = parse_input(input_line)
    compacted = compact(stack)
    result = checksum(compacted)

    return result


def main():
    with open("09/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))[0]

    print(solve(test_input))


if __name__ == "__main__":
    main()
