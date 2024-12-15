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
                print("[", end="")
            elif p - 1 in boxes:
                print("]", end="")
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
                    world[complex(x * 2, y)] = c
                    world[complex(x * 2 + 1, y)] = c
                else:
                    world[complex(x * 2, y)] = "."
                    world[complex(x * 2 + 1, y)] = "."
                if c == "O":
                    boxes.add(complex(x * 2, y))
                if c == "@":
                    robot = complex(x * 2, y)

        else:
            instructions.extend(line)

    # draw(world, boxes, robot)
    for instruction in instructions:
        # print(instruction)
        d = {"^": -1j, ">": 1 + 0j, "v": 1j, "<": -1 + 0j}[instruction]
        boxes_to_move: set[complex] = set()
        frontier: list[complex] = [robot + d]

        while not any(world[p] == "#" for p in frontier):
            new_frontier: list[complex] = []
            for p in frontier:
                if p in boxes:
                    new_frontier.append(p + d)
                    new_frontier.append(p + 1 + d)
                    boxes_to_move.add(p)
                if p - 1 in boxes:
                    new_frontier.append(p - 1 + d)
                    new_frontier.append(p + d)
                    boxes_to_move.add(p - 1)
            # Don't push the same box twice
            for b in boxes_to_move:
                if b in new_frontier:
                    new_frontier.remove(b)
                if b + 1 in new_frontier:
                    new_frontier.remove(b + 1)
            if not any(new_frontier):
                break
            frontier = new_frontier
        else:
            continue

        for box in boxes_to_move:
            assert box in boxes
            boxes.remove(box)
        for box in boxes_to_move:
            boxes.add(box + d)
        robot = robot + d
    draw(world, boxes, robot)

    print()
    return score(boxes)


def main():
    with open("15/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
