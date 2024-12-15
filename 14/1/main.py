import re


def solve(input_lines: list[str], w: int = 101, h: int = 103):
    steps = 100

    robot_re = re.compile(r"p=(?P<x>\d+),(?P<y>\d+)\sv=(?P<vx>-?\d+),(?P<vy>-?\d+)")

    quadrants = [0, 0, 0, 0]

    for line in input_lines:
        assert (match := robot_re.match(line)) is not None
        x, y, vx, vy = map(int, match.groups())
        fx = (x + vx * steps + w * steps) % w
        fy = (y + vy * steps + h * steps) % h

        if fx < w // 2:
            if fy < h // 2:
                quadrants[0] += 1
            elif fy > h // 2:
                quadrants[1] += 1
        elif fx > w // 2:
            if fy < h // 2:
                quadrants[2] += 1
            elif fy > h // 2:
                quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def main():
    with open("14/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
