from main import solve


def test_main():
    assert (
        solve(
            [
                "ka-co",
                "ta-co",
                "de-co",
                "ta-ka",
                "de-ta",
                "ka-de",
            ]
        )
        == "co,de,ka,ta"
    )
