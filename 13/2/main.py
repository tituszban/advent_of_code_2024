import re
from fractions import Fraction


class ClawMachine:
    button_re = re.compile(r"^Button (?:A|B): X\+(?P<x>\d+), Y\+(?P<y>\d+)$")
    prize_re = re.compile(r"^Prize: X=(?P<x>\d+), Y=(?P<y>\d+)$")

    def __init__(self, button_a: str, button_b: str, prize: str):
        assert (ma := self.button_re.match(button_a))
        self._Ax = Fraction(int(ma.group("x")))
        self._Ay = Fraction(int(ma.group("y")))
        assert (mb := self.button_re.match(button_b))
        self._Bx = Fraction(int(mb.group("x")))
        self._By = Fraction(int(mb.group("y")))
        assert (mp := self.prize_re.match(prize))
        self._X = Fraction(int(mp.group("x")) + 10000000000000)
        self._Y = Fraction(int(mp.group("y")) + 10000000000000)

    def solve(self):
        """
        X = Ax * a + Bx * b
        Y = Ay * a + By * b

        (X - Bx * b) / Ax = a
        Y = Ay * ((X - Bx * b) / Ax) + By * b
        Y = Ay / Ax * X - Ay / Ax * Bx * b + By * b
        Y - Ay / Ax * X = (By - Ay / Ax * Bx) * b
        b = (Y - Ay / Ax * X) / (By - Ay / Ax * Bx)
        """
        b = (self._Y - self._Ay / self._Ax * self._X) / (
            self._By - self._Ay / self._Ax * self._Bx
        )
        a = (self._X - self._Bx * b) / self._Ax
        return a, b


def is_whole(n: Fraction):
    return n.denominator == 1


def solve(input_lines: list[str]):
    total = 0
    for i in range(0, len(input_lines), 4):
        claw_machine = ClawMachine(*input_lines[i : i + 3])
        a, b = claw_machine.solve()

        if is_whole(a) and is_whole(b):
            total += int(a * 3 + b)

    return total


def main():
    with open("13/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
