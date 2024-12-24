from operator import or_, and_, xor
import re
from typing import Callable


def to_num(vals: dict[str, bool], prefix: str):
    result = 0
    for name, v in vals.items():
        if name.startswith(prefix):
            result += int(v) << int(name[1:])
    return result


def evaluate_adder(
    x: int, y: int, gates: dict[str, tuple[Callable[[bool, bool], bool], str, str]]
) -> int:
    gate_vals: dict[str, bool] = {}

    def eval(val: str) -> bool:
        if val in gate_vals:
            return gate_vals[val]
        if val.startswith("x"):
            return bool((x >> int(val[1:])) & 1)
        if val.startswith("y"):
            return bool((y >> int(val[1:])) & 1)
        gate, a, b = gates[val]
        res = gate(eval(a), eval(b))
        gate_vals[val] = res
        return res

    for gate in gates:
        eval(gate)

    return to_num(gate_vals, "z")


def solve(input_lines: list[str]):
    inputs: dict[str, bool] = {}
    gates: dict[str, tuple[Callable[[bool, bool], bool], str, str]] = {}
    remap: dict[str, str] = {
        "qwf": "cnk",
        "cnk": "qwf",
        "msq": "z39",
        "z39": "msq",
        "mps": "z27",
        "z27": "mps",
        "vhm": "z14",
        "z14": "vhm",
    }

    for line in input_lines:
        if not line:
            continue
        if m := re.match(r"([\w\d]{3}): (\d)", line):
            inputs[m.group(1)] = bool(int(m.group(2)))
        elif m := re.match(
            r"([\w\d]{3}) (AND|OR|XOR) ([\w\d]{3}) -> ([\w\d]{3})", line
        ):
            gates[remap.get(m.group(4), m.group(4))] = (
                {"OR": or_, "AND": and_, "XOR": xor}[m.group(2)],
                m.group(1) if m.group(1) > m.group(3) else m.group(3),
                m.group(3) if m.group(1) > m.group(3) else m.group(1),
            )
        else:
            assert False, f"Invalid line: {line}"

    name_mappings = {}
    for gate in gates:
        g, a, b = gates[gate]
        if a[0] in ("x", "y") and b[0] in ("x", "y"):
            assert a[1:] == b[1:]
            if g == and_:
                name_mappings[gate] = f"C{a[1:]}"
            if g == xor:
                name_mappings[gate] = f"V{a[1:]}"

    for gate in gates:
        g, a, b = gates[gate]
        am = name_mappings.get(a, a)
        bm = name_mappings.get(b, b)
        gm = name_mappings.get(gate, gate)
        if am[0] == "C" and g == or_:
            assert bm == b
            assert gm == gate
            name_mappings[b] = f"B{am[1:]}"
            name_mappings[gate] = f"A{int(am[1:]) + 1:02d}"
        if bm[0] == "C" and g == or_:
            assert am == a
            assert gm == gate
            name_mappings[a] = f"B{bm[1:]}"
            name_mappings[gate] = f"A{int(bm[1:]) + 1:02d}"

    lines = []
    for gate in gates:
        g, a, b = gates[gate]
        gm = name_mappings.get(gate, gate)
        am = name_mappings.get(a, a)
        bm = name_mappings.get(b, b)
        l1, l2 = sorted([am, bm])
        lines.append(f"{l1} {g.__name__.rstrip("_")} {l2} -> {gm}\n")
    with open("24/mapped_gates.txt", "w") as f:
        f.writelines(sorted(lines))

    suspects = set()

    for i in range(45):
        v = evaluate_adder(1 << i, 1 << i, gates)
        if v != (1 << i) * 2:
            suspects.add(i)
        print(f"{i:02d}: {v:046b}")
    print()
    for i in range(45):
        v = evaluate_adder(1 << i, 0, gates)
        if v != (1 << i):
            suspects.add(i)
        print(f"{i:02d}: {v:046b}")
    print()
    for i in range(45):
        v = evaluate_adder(0, 1 << i, gates)
        if v != (1 << i):
            suspects.add(i)
        print(f"{i:02d}: {v:046b}")

    return ','.join(sorted(remap.keys()))


def main():
    with open("24/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
