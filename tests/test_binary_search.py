"""Smoke test for binary_search.py -- repocurator feature 002.

binary_search.py sits at the repository root with no package structure, so
this file puts that root on sys.path before importing it. The module's own
__main__ block already runs 1000 random rounds and prints a verdict for each,
but it never raises or exits non-zero on a wrong answer -- a broken
implementation would still print a passing-looking log. This test calls
`binary_search` directly against known present and absent values, so a
regression actually fails the build.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from binary_search import binary_search

SORTED_LIST = [1, 5, 6, 8, 11, 34, 40, 55]


def test_binary_search_finds_every_present_value():
    for index, value in enumerate(SORTED_LIST):
        assert binary_search(SORTED_LIST, value) == index


def test_binary_search_returns_none_for_an_absent_value():
    assert binary_search(SORTED_LIST, 7) is None
