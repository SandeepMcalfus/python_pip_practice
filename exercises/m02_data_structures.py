"""
Module 2 - Data Structures: lists, dicts, sets, tuples, comprehensions.
"""


def remove_duplicates(items: list) -> list:
    """Remove duplicates but KEEP the original order.  [3, 1, 3, 2, 1] -> [3, 1, 2]"""
    raise NotImplementedError


def word_frequency(text: str) -> dict:
    """Count each word, lower-cased.  "the cat and the hat" -> {"the": 2, "cat": 1, "and": 1, "hat": 1}"""
    raise NotImplementedError


def merge_dicts(a: dict, b: dict) -> dict:
    """Merge two dicts of numbers. If a key is in both, ADD the values.
    {"x": 1, "y": 2} + {"y": 3, "z": 4} -> {"x": 1, "y": 5, "z": 4}
    Do not modify the inputs."""
    raise NotImplementedError


def common_elements(a: list, b: list) -> list:
    """Return elements present in both lists, sorted ascending, no duplicates."""
    raise NotImplementedError


def flatten(nested: list) -> list:
    """Flatten ONE level.  [[1, 2], [3], [], [4, 5]] -> [1, 2, 3, 4, 5]
    Try to do it as a list comprehension."""
    raise NotImplementedError


def group_by_length(words: list) -> dict:
    """Group words by length.  ["hi", "yo", "cat"] -> {2: ["hi", "yo"], 3: ["cat"]}
    Keep words in their original order inside each group."""
    raise NotImplementedError
