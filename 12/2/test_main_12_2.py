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
        == 80
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
        == 436
    )


def test_main_e():
    assert (
        solve(
            [
                "EEEEE",
                "EXXXX",
                "EEEEE",
                "EXXXX",
                "EEEEE",
            ]
        )
        == 236
    )


def test_main_ab():
    assert (
        solve(
            [
                "AAAAAA",
                "AAABBA",
                "AAABBA",
                "ABBAAA",
                "ABBAAA",
                "AAAAAA",
            ]
        )
        == 368
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
        == 1206
    )
