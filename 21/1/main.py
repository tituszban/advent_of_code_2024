from itertools import permutations
from functools import cache

numpad = "789\n456\n123\n 0A"

dir_pad = " ^A\n<v>"


@cache
def move(from_c: str, to_c: str, pad: str = numpad) -> list[str]:
    numpad_d = {
        c: (x + y * 1j)
        for y, row in enumerate(pad.split("\n"))
        for x, c in enumerate(row)
    }
    d = numpad_d[to_c] - numpad_d[from_c]
    move = [
        *([">"] * int(d.real) if d.real > 0 else ["<"] * abs(int(d.real))),
        *(["v"] * int(d.imag) if d.imag > 0 else ["^"] * abs(int(d.imag))),
    ]
    if not move:
        return ["A"]
    possible_actions = list(permutations(move))

    good_actions = []
    for seq in possible_actions:
        p = numpad_d[from_c]
        bad = numpad_d[" "]
        goal = numpad_d[to_c]
        for c in seq:
            p += {"v": 1j, "^": -1j, ">": 1 + 0j, "<": -1 + 0j}[c]
            if p == bad:
                break
            if p == goal:
                good_actions.append(''.join(seq))
                break

    return [a + "A" for a in good_actions]


def numpad_move(code: str, pad: str = numpad) -> list[str]:
    pointer = "A"
    results = [""]

    for c in code:
        possibilities = move(pointer, c, pad)
        results = [result + "".join(p) for p in possibilities for result in results]

        pointer = c
    return results


def generate_keypad_lookup():
    lookup = {}
    for c1 in "v^<>A":
        for c2 in "v^<>A":
            cl: str | None = None
            for s1 in move(c1, c2, dir_pad):
                if cl is None:
                    cl = s1
                if len(s1) < len(cl):
                    cl = s1
            lookup[(c1, c2)] = cl
    l = {k: len(v) for k, v in lookup.items()}
    return l


def generate_second_order_keyboard_lookup(lookup_1st: dict[tuple[str, str], int]):
    lookup = {}
    for c1 in "v^<>A":
        for c2 in "v^<>A":
            cl: int | None = None
            for s in move(c1, c2, dir_pad):
                total = 0
                s = ["A", *s]
                for s1, s2 in zip(["A", *s], s):
                    total += lookup_1st[(s1, s2)]
                if cl is None:
                    cl = total
                if total < cl:
                    cl = total
            lookup[(c1, c2)] = cl - 1
    return lookup


def generate_lookup(lookup_nums: dict[tuple[str, str], int]):
    lookup = {}
    for c1 in "A0123456789":
        for c2 in "A0123456789":
            if c1 == c2:
                continue
            cl: int | None = None
            for s in move(c1, c2, numpad):
                total = 0
                for s1, s2 in zip(["A", *s], s):
                    total += lookup_nums[(s1, s2)]
                if cl is None:
                    cl = total
                if total < cl:
                    cl = total
            lookup[(c1, c2)] = cl
    return lookup


def solve(input_lines: list[str]):
    l1 = generate_keypad_lookup()
    l2 = generate_second_order_keyboard_lookup(l1)
    l = generate_lookup(l2)

    result = 0
    for code in input_lines:
        c = 0
        for s1, s2 in zip(["A", *code], code):
            c += l[(s1, s2)]
        result += c * int(code.replace("A", ""))

    return result


def main():
    with open("21/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
