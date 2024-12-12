from main import solve


def test_main_small():
    assert (
        solve(
            [
                "AAAA",
                "BBCD",
                "BBCC",
                "EEEC",
            ]
        )
        == 140
    )


def test_main_holes():
    assert (
        solve(
            [
                "OOOOO",
                "OXOXO",
                "OOOOO",
                "OXOXO",
                "OOOOO",
            ]
        )
        == 772
    )


def test_main_big():
    assert (
        solve(
            [
                "RRRRIICCFF",
                "RRRRIICCCF",
                "VVRRRCCFFF",
                "VVRCCCJFFF",
                "VVVVCJJCFE",
                "VVIVCCJJEE",
                "VVIIICJJEE",
                "MIIIIIJJEE",
                "MIIISIJEEE",
                "MMMISSJEEE",
            ]
        )
        == 1930
    )
