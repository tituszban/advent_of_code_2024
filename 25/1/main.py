def solve(input_lines: list[str]):
    locks: list[set[str]] = []
    keys: list[set[str]] = []

    for line in input_lines:
        schematic = {
            str(i)+str(j) 
            for i, row in enumerate(line.split("\n")) 
            for j, cell in enumerate(row) 
            if cell == "#"
        }
        if "00" in schematic:
            locks.append(schematic)
        else:
            keys.append(schematic)

    count = 0
    for lock in locks:
        for key in keys:
            if not lock & key:
                count += 1
    
    return count



def main():
    with open("25/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.read().split("\n\n")))

    print(solve(test_input))


if __name__ == "__main__":
    main()
