import networkx as nx

def solve(input_lines: list[str]):
    graph = nx.Graph()

    pairs = [tuple(line.split("-")) for line in input_lines]

    graph.add_edges_from(pairs)

    triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]

    with_t = [triangle for triangle in triangles if any(node.startswith("t") for node in triangle)]
    
    return len(with_t)


def main():
    with open("23/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
