import networkx as nx

def solve(input_lines: list[str]):
    graph = nx.Graph()

    pairs = [tuple(line.split("-")) for line in input_lines]

    graph.add_edges_from(pairs)

    largest_group = max(nx.find_cliques(graph), key=len)

    result = ",".join(sorted(largest_group))

    return result



def main():
    with open("23/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
