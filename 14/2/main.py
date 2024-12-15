import re
import cv2
import numpy as np

"""
Vertical Clusters:
76
179
282
385
488
591
694
797
900
"""


def show(points: list[tuple[int, int]], n: int, w: int = 101, h: int = 103):
    img = np.zeros((w, h), np.dtype("uint8"))

    for p in points:
        img[p] = 255

    img = cv2.resize(img, (h * 10, w * 10), interpolation=cv2.INTER_NEAREST)
    # cv2.imshow(f"image {n}", img)
    cv2.imwrite(f"14/2/.imgs/{n}.png", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def solve(input_lines: list[str], w: int = 101, h: int = 103):
    robot_re = re.compile(r"p=(?P<x>\d+),(?P<y>\d+)\sv=(?P<vx>-?\d+),(?P<vy>-?\d+)")

    data: list[tuple[tuple[int, int], tuple[int, int]]] = [
        (
            (int(match.group("x")), int(match.group("y"))),
            (int(match.group("vx")), int(match.group("vy"))),
        )
        for line in input_lines
        if (match := robot_re.match(line))
    ]
    points = [d[0] for d in data]
    velocities = [d[1] for d in data]

    i = 0
    show(points, i, w, h)
    i = 76
    points = [
        ((x + vx * 76 + w * 76) % w, (y + vy * 76 + h * 76) % h)
        for (x, y), (vx, vy) in zip(points, velocities)
    ]
    step_size = 103

    for _ in range(1000):
        i += step_size
        points = [
            ((x + vx * step_size + w * step_size) % w, (y + vy * step_size + h * step_size) % h)
            for (x, y), (vx, vy) in zip(points, velocities)
        ]
        show(points, i, w, h)


def main():
    with open("14/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
