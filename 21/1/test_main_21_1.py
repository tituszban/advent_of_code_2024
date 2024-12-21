from main import solve


def test_main():
    assert solve([
"029A",
"980A",
"179A",
"456A",
"379A",
    ]) == 126384

"""

   10            8           8         4     6       9           1 4     9           1 1 7
S: <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
S: v   <  < A    >  > ^   A  <    A    >  A  v   A   <    ^   A  A >  A  <    v  A   A A >  ^   A
S: <             A           ^         A     >       ^           ^ A     v           v v A
S: 0                         2               9                           A

"""