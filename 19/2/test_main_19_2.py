from main import solve


def test_main():
    assert (
        solve(
            [
                "r, wr, b, g, bwu, rb, gb, br",
                "",
                "brwrr",
                "bggr",
                "gbbr",
                "rrbgbr",
                "ubwu",
                "bwurrg",
                "brgr",
                "bbrgwb",
            ]
        )
        == 16
    )
