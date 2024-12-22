from main import solve


def test_main_1():
    assert solve(["123"], 10) == 5908254


def test_main_2():
    assert (
        solve(
            [
                "1",
                "10",
                "100",
                "2024",
            ]
        )
        == 37327623
    )
