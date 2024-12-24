from operator import or_, and_, xor
import re
from typing import Callable
from functools import cache

def solve(input_lines: list[str]):
    inputs: dict[str, bool] = {}
    gates: dict[str, tuple[Callable[[bool, bool], bool], str, str]] = {}

    for line in input_lines:
        if not line:
            continue
        if (m := re.match(r"([\w\d]{3}): (\d)", line)):
            inputs[m.group(1)] = bool(int(m.group(2)))
        elif (m := re.match(r"([\w\d]{3}) (AND|OR|XOR) ([\w\d]{3}) -> ([\w\d]{3})", line)):
            gates[m.group(4)] = ({"OR": or_, "AND": and_, "XOR": xor}[m.group(2)], m.group(1), m.group(3))
        else:
            assert False, f"Invalid line: {line}"


    @cache
    def eval(val: str) -> bool:
        if val in inputs:
            return inputs[val]
        gate, a, b = gates[val]
        return gate(eval(a), eval(b))
    
    gate_results: dict[int, bool] = {}

    for g in gates:
        if g.startswith("z"):
            gate_results[int(g[1:])] = eval(g)

    result = 0
    for i, v in gate_results.items():
        result += int(v) << i
    
    return result


def main():
    with open("24/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
