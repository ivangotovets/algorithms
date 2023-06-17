"""Non recursive implementation of a DFS algorithm."""
from __future__ import annotations


def depth_first_search(graph: dict, start: str) -> set[str]:

    explored, stack = set(start), [start]

    while stack:
        v = stack.pop()
        explored.add(v)

        for adj in reversed(graph[v]):
            if adj not in explored:
                stack.append(adj)
    return explored


G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}


print(depth_first_search(G, "A"))
