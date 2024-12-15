def draw(world: dict[complex, str], boxes: set[complex], robot: complex):
    min_x = int(min(p.real for p in world))
    max_x = int(max(p.real for p in world))
    min_y = int(min(p.imag for p in world))
    max_y = int(max(p.imag for p in world))

    print()
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            p = complex(x, y)
            if p in boxes:
                print("O", end="")
            elif p == robot:
                print("@", end="")
            else:
                print(world[p], end="")
        print()


def score(boxes: set[complex]):
    return int(sum(b.real + b.imag * 100 for b in boxes))


def solve(input_lines: list[str]):
    world: dict[complex, str] = {}
    boxes: set[complex] = set()
    robot: complex = 0
    instructions: list[str] = []

    reading_world = True
    for y, line in enumerate(input_lines):
        if line == "":
            reading_world = False
            continue

        if reading_world:
            for x, c in enumerate(line):
                if c == "#":
                    world[complex(x, y)] = c
                else:
                    world[complex(x, y)] = "."
                if c == "O":
                    boxes.add(complex(x, y))
                if c == "@":
                    robot = complex(x, y)

        else:
            instructions.extend(line)

    for instruction in instructions:
        d = {"^": -1j, ">": 1 + 0j, "v": 1j, "<": -1 + 0j}[instruction]
        boxes_to_move: set[complex] = set()
        i = 1
        while world[p := (robot + d * i)] != "#" and p in boxes:
            boxes_to_move.add(p)
            i += 1
        if world[robot + d * i] == "#":
            continue
        for box in boxes_to_move:
            boxes.remove(box)
        for box in boxes_to_move:
            boxes.add(box + d)
        robot = robot + d
    # draw(world, boxes, robot)

    print()
    return score(boxes)


def main():
    with open("15/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
