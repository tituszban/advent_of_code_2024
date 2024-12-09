from __future__ import annotations
from collections import deque


class Node:
    def __init__(self, idx: int | None, count: int, next: Node | None = None, prev: Node | None = None):
        self.idx = idx
        self.count = count
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node({self.idx}, {self.count})"

    def mark_empty(self):
        self.count = 0
        self.next = None
        self.prev = None

    def insert(self, other: Node):
        assert self.idx is None
        assert other.idx is not None
        assert other.count <= self.count
        assert self.next is not None
        remaining = self.count - other.count
        if remaining > 0:
            if self.prev:
                self.prev.next = other
            other.prev = self.prev
            other.next = self
            self.prev = other
            self.count = remaining
        else:
            if self.prev:
                self.prev.next = other
            other.prev = self.prev
            other.next = self.next
            self.next.prev = other
            self.mark_empty()

    def pop(self):
        assert self.idx is not None
        assert self.count > 0
        assert self.prev is not None

        space_left = Node(None, self.count, self.next, self.prev)
        self.prev.next = space_left
        if self.next:
            self.next.prev = space_left

        return self, space_left


def parse_input(input_line: str):
    is_data = True
    idx = 0
    stack: deque[tuple[int | None, int]] = deque()
    for d in input_line:
        if is_data:
            stack.append((idx, int(d)))
            idx += 1
        else:
            stack.append((None, int(d)))
        is_data = not is_data

    return stack


def to_linked_list(stack: deque[tuple[int | None, int]]):
    node = None
    tail = None
    while stack:
        idx, count = stack.pop()
        if count == 0:
            continue
        n = Node(idx, count, node)
        if node is None:
            tail = n
        node = n

    head = node

    while node.next:
        node.next.prev = node
        node = node.next

    return head, tail


def print_linked_list(head: Node, pl: Node, pr: Node):
    s1 = ""
    s2 = ""
    while head:
        s1 += ("l" if head == pl else ("r" if head == pr else " ")) * head.count
        s2 += (str(head.idx) if head.idx is not None else ".") * head.count

        head = head.next
    print(s1)
    print(s2)


def compact(stack: deque[tuple[int | None, int]]):
    head, tail = to_linked_list(stack)
    p_left, p_right = head, tail

    # print("")
    while True:
        # print_linked_list(head, p_left, p_right)
        if p_left == p_right:
            h = head
            result = []
            while h:
                result.append((h.idx, h.count))
                h = h.next
            return result

        if p_left.idx is not None:
            assert p_left.next
            p_left = p_left.next
            continue
        if p_right.idx is None:
            p_right = p_right.prev
            continue

        insert_to = p_left
        while insert_to is not None and insert_to != p_right and (insert_to.idx is not None or insert_to.count < p_right.count):
            insert_to = insert_to.next

        if insert_to is None or insert_to == p_right:
            p_right = p_right.prev
            continue

        node, p_right = p_right.pop()

        insert_to.insert(node)
        if insert_to == p_left:
            p_left = node


def checksum(compacted: list[tuple[int, int]]):
    i = 0
    total = 0
    for idx, count in compacted:
        for _ in range(count):
            if idx is not None:
                total += idx * i
            i += 1
    return total


def solve(input_line: str):
    stack = parse_input(input_line)
    compacted = compact(stack)
    result = checksum(compacted)

    return result


def main():
    with open("09/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))[0]

    print(solve(test_input))


if __name__ == "__main__":
    main()
