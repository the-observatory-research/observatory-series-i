"""Checks for the post-archive 1B example helper, not historical tests."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tools"))
from check_experiment_1b import simple_paths, reference_targets

class TestExplicitBaselineReference(unittest.TestCase):
    def test_path_enumeration(self):
        self.assertEqual(simple_paths("A", "E"), [
            ("A", "B", "C", "D", "E"),
            ("A", "D", "E"),
        ])

    def test_b_unavailable(self):
        self.assertEqual(simple_paths("A", "C", frozenset({"B"})), [("A", "D", "C")])

    def test_d_to_a_no_route(self):
        self.assertEqual(simple_paths("D", "A"), [])

    def test_c_to_e_requires_d(self):
        self.assertEqual(simple_paths("C", "E", frozenset({"D"})), [])

    def test_no_repeated_nodes(self):
        for path in simple_paths("A", "E"):
            self.assertEqual(len(path), len(set(path)))

    def test_four_targets(self):
        self.assertEqual(len(reference_targets()),4)

if __name__ == "__main__": unittest.main()
