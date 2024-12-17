class Computer:
    def __init__(self, reg_a: int, reg_b: int, reg_c: int, program: list[int]):
        self._program = program
        self._reg_a = reg_a
        self._reg_b = reg_b
        self._reg_c = reg_c
        self._instruction_pointer = 0
        self._output = []

    def _combo(self, operand: int):
        return {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self._reg_a,
            5: self._reg_b,
            6: self._reg_c,
        }[operand]

    def _adv(self, operand: int):
        numerator = self._reg_a
        denominator = 2 ** self._combo(operand)
        self._reg_a = numerator // denominator

        self._instruction_pointer += 2

    def _bxl(self, operand: int):
        self._reg_b = self._reg_b ^ operand
        self._instruction_pointer += 2

    def _bst(self, operand: int):
        self._reg_b = self._combo(operand) % 8
        self._instruction_pointer += 2

    def _jnz(self, operand: int):
        if self._reg_a == 0:
            self._instruction_pointer += 2
            return
        self._instruction_pointer = operand

    def _bxc(self, operand: int):
        self._reg_b = self._reg_b ^ self._reg_c
        self._instruction_pointer += 2

    def _out(self, operand: int):
        self._output.append(self._combo(operand) % 8)
        self._instruction_pointer += 2

    def _bdv(self, operand: int):
        numerator = self._reg_a
        denominator = 2 ** self._combo(operand)
        self._reg_b = numerator // denominator

        self._instruction_pointer += 2

    def _cdv(self, operand: int):
        numerator = self._reg_a
        denominator = 2 ** self._combo(operand)
        self._reg_c = numerator // denominator

        self._instruction_pointer += 2

    def run(self):
        while self._instruction_pointer + 1 < len(self._program):
            opcode, operand = (
                self._program[self._instruction_pointer],
                self._program[self._instruction_pointer + 1],
            )
            {
                0: self._adv,
                1: self._bxl,
                2: self._bst,
                3: self._jnz,
                4: self._bxc,
                5: self._out,
                6: self._bdv,
                7: self._cdv,
            }[opcode](operand)

        return ",".join(map(str, self._output))


def solve(input_lines: list[str]):
    computer = Computer(
        int(input_lines[0].split(": ")[1]),
        int(input_lines[1].split(": ")[1]),
        int(input_lines[2].split(": ")[1]),
        list(map(int, input_lines[4].split(": ")[1].split(","))),
    )
    return computer.run()


def main():
    with open("17/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
