from collections import defaultdict
from functools import cache


@cache
def calc_next(n: int) -> int:
    x1 = ((n * 64) ^ n) % 16777216
    x2 = ((x1 // 32) ^ x1) % 16777216
    x3 = ((x2 * 2048) ^ x2) % 16777216
    return x3


def solve(input_lines: list[str], repeat: int = 2000) -> int:
    sequences: list[dict[int, set[tuple[int, int, int, int]]]] = []
    for secret in input_lines:
        n = 0
        s = int(secret)
        buffer = [s % 10]
        secret_seqs = defaultdict(set)
        all_seqs = set()
        while n < repeat:
            s = calc_next(s)
            v = s % 10
            buffer.append(v)
            if len(buffer) > 4:
                diffs = tuple([v2 - v1 for v1, v2 in zip(buffer, buffer[1:])])
                if diffs not in all_seqs:
                    secret_seqs[v].add(diffs)
                    all_seqs.add(diffs)
                buffer.pop(0)

            n += 1
        sequences.append(secret_seqs)

    sequence_scores: dict[tuple[int, int, int, int], int] = defaultdict(int)

    for seqs in sequences:
        for k, v in seqs.items():
            for seq in v:
                sequence_scores[seq] += k

    result = max(sequence_scores, key=lambda k: sequence_scores[k])

    return sequence_scores[result]


def main():
    with open("22/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
