from main import solve


def test_main():
    assert solve(
        [
            "Register A: 2024",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,3,5,4,3,0",
        ]
    ) == 117440
