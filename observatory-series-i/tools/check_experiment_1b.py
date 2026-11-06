#!/usr/bin/env python3
"""Post-archive reference checker for the explicit Series I 1B graph.

This helper was made for portfolio packaging. It did NOT run during
the original Series I experiment and does not rescore historical trials.
"""
from __future__ import annotations
from collections.abc import Iterator

EDGES: dict[str, tuple[str, ...]] = {
    "A": ("B", "D"),
    "B": ("C",),
    "C": ("D",),
    "D": ("C", "E"),
    "E": ("B",),
}

def simple_paths(start: str, end: str, unavailable: frozenset[str] = frozenset()) -> list[tuple[str, ...]]:
    """Enumerate directed paths without repeated nodes; omit unavailable nodes."""
    if start in unavailable or end in unavailable:
        return []
    completed: list[tuple[str, ...]] = []
    def walk(node: str, path: tuple[str, ...]) -> None:
        if node == end:
            completed.append(path)
            return
        for next_node in EDGES[node]:
            if next_node not in path and next_node not in unavailable:
                walk(next_node, path+(next_node,))
    walk(start,(start,))
    return sorted(completed)

def reference_targets() -> dict[str, object]:
    """Four declared 1B scoring targets, without scoring model output."""
    return {
        "q1_a_to_e": simple_paths("A", "E"),
        "q2_a_to_c_no_b": simple_paths("A", "C", frozenset({"B"})),
        "q3_d_to_a_possible": bool(simple_paths("D", "A")),
        "q4_c_to_e_without_d_possible": bool(simple_paths("C", "E", frozenset({"D"}))),
    }

if __name__ == "__main__":
    import json
    print(json.dumps(reference_targets(), indent=2))
