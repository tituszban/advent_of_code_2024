from main import solve


def test_main_1():
    assert solve(["123"], 10) == 6


def test_main_2():
    assert (
        solve(
            [
                "1",
                "2",
                "3",
                "2024",
            ]
        )
        == 23
    )
