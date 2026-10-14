"""
Module 2 - Data Structures: lists, dicts, sets, tuples, comprehensions.
"""
from collections import Counter, defaultdict, deque, namedtuple

Point = namedtuple("Point", ["x", "y"])


def remove_duplicates(items: list) -> list:
    """Remove duplicates but KEEP the original order.  [3, 1, 3, 2, 1] -> [3, 1, 2]"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def word_frequency(text: str) -> dict:
    """Count each word, lower-cased.  "the cat and the hat" -> {"the": 2, "cat": 1, "and": 1, "hat": 1}"""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def merge_dicts(a: dict, b: dict) -> dict:
    """Merge two dicts of numbers. If a key is in both, ADD the values.
    {"x": 1, "y": 2} + {"y": 3, "z": 4} -> {"x": 1, "y": 5, "z": 4}
    Do not modify the inputs."""
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, 0) + value
    return result


def common_elements(a: list, b: list) -> list:
    """Return elements present in both lists, sorted ascending, no duplicates."""
    return sorted(set(a) & set(b))


def flatten(nested: list) -> list:
    """Flatten ONE level.  [[1, 2], [3], [], [4, 5]] -> [1, 2, 3, 4, 5]
    Try to do it as a list comprehension."""
    return [item for sub in nested for item in sub]


def group_by_length(words: list) -> dict:
    """Group words by length.  ["hi", "yo", "cat"] -> {2: ["hi", "yo"], 3: ["cat"]}
    Keep words in their original order inside each group."""
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


# ---------------------------------------------------------------------------
# Lists  (indexing, slicing, append/insert/pop, sort vs sorted, enumerate)
# ---------------------------------------------------------------------------

def rotate_list(items: list, k: int) -> list:
    """Rotate RIGHT by k steps.  [1, 2, 3, 4, 5], 2 -> [4, 5, 1, 2, 3]
    k may be larger than the list. Empty list -> [].  Hint: slicing and k % len."""
    if not items:
        return []
    k = k % len(items)
    return items[-k:] + items[:-k] if k else items[:]


def chunk(items: list, size: int) -> list:
    """Split into chunks of `size`; the last chunk may be shorter.
    [1, 2, 3, 4, 5], 2 -> [[1, 2], [3, 4], [5]]   Hint: range(0, len, size)."""
    return [items[i:i + size] for i in range(0, len(items), size)]


def second_largest(numbers: list) -> int:
    """Second largest DISTINCT value.  [4, 1, 4, 3] -> 3
    Raise ValueError if there are fewer than 2 distinct values."""
    distinct = sorted(set(numbers), reverse=True)
    if len(distinct) < 2:
        raise ValueError("need at least 2 distinct values")
    return distinct[1]


def running_total(numbers: list) -> list:
    """Cumulative sums.  [1, 2, 3, 4] -> [1, 3, 6, 10]"""
    result = []
    total = 0
    for n in numbers:
        total += n
        result.append(total)
    return result


def move_zeros_to_end(numbers: list) -> list:
    """Move all 0s to the end, keeping the order of the other numbers.
    [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]   Return a new list."""
    non_zeros = [n for n in numbers if n != 0]
    zeros = [0] * (len(numbers) - len(non_zeros))
    return non_zeros + zeros


def find_all_indexes(items: list, target) -> list:
    """Every index where target appears.  ["a", "b", "a"], "a" -> [0, 2]
    Hint: enumerate()."""
    return [i for i, item in enumerate(items) if item == target]


# ---------------------------------------------------------------------------
# Tuples  (packing / unpacking, immutability, tuples as dict keys, zip)
# ---------------------------------------------------------------------------

def min_max(numbers: list) -> tuple:
    """Return (smallest, largest).  [3, 7, 1, 9] -> (1, 9)
    Raise ValueError for an empty list."""
    if not numbers:
        raise ValueError("min_max() of an empty list")
    return (min(numbers), max(numbers))


def sort_by_second(pairs: list) -> list:
    """Sort a list of tuples by their SECOND item.
    [("a", 3), ("b", 1), ("c", 2)] -> [("b", 1), ("c", 2), ("a", 3)]
    Hint: sorted(..., key=lambda p: p[1])."""
    return sorted(pairs, key=lambda p: p[1])


def unzip_pairs(pairs: list) -> tuple:
    """Split pairs into two tuples.  [(1, "a"), (2, "b")] -> ((1, 2), ("a", "b"))
    Empty list -> ((), ()).   Hint: zip(*pairs)."""
    if not pairs:
        return ((), ())
    first, second = zip(*pairs)
    return (first, second)


def count_coordinates(points: list) -> dict:
    """Count how often each (x, y) point appears — tuples can be dict keys!
    [(0, 0), (1, 2), (0, 0)] -> {(0, 0): 2, (1, 2): 1}"""
    counts = {}
    for point in points:
        counts[point] = counts.get(point, 0) + 1
    return counts


# ---------------------------------------------------------------------------
# Dictionaries  (get, items, setdefault, sorting, nested dicts)
# ---------------------------------------------------------------------------

def invert_dict(d: dict) -> dict:
    """Swap keys and values.  {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    Values are guaranteed unique."""
    return {value: key for key, value in d.items()}


def dict_from_lists(keys: list, values: list) -> dict:
    """Pair keys with values.  ["a", "b"], [1, 2] -> {"a": 1, "b": 2}
    If the lists differ in length, ignore the extras.  Hint: dict(zip(...))."""
    return dict(zip(keys, values))


def filter_by_value(d: dict, minimum) -> dict:
    """Keep only entries whose value is >= minimum.
    {"a": 5, "b": 2, "c": 9}, 5 -> {"a": 5, "c": 9}"""
    return {key: value for key, value in d.items() if value >= minimum}


def sort_dict_by_value(d: dict) -> list:
    """Return the KEYS sorted by value, highest first.  Ties: keep insertion order.
    {"x": 2, "y": 9, "z": 5} -> ["y", "z", "x"]"""
    return sorted(d, key=lambda key: d[key], reverse=True)


def top_n_words(text: str, n: int) -> list:
    """The n most common lower-cased words as (word, count), most common first.
    Ties: the word seen first wins.
    "a b a c b a", 2 -> [("a", 3), ("b", 2)]   Hint: collections.Counter."""
    return Counter(text.lower().split()).most_common(n)


def safe_get(data: dict, path: list, default=None):
    """Walk a nested dict by a list of keys; return default if any key is missing.
    {"a": {"b": {"c": 1}}}, ["a", "b", "c"] -> 1
    {"a": {"b": {}}},       ["a", "x"]      -> None"""
    current = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def average_scores(students: dict) -> dict:
    """Average score per student, rounded to 1 decimal.  Empty list -> 0.0
    {"ana": [90, 80], "bo": [70]} -> {"ana": 85.0, "bo": 70.0}"""
    result = {}
    for name, scores in students.items():
        if scores:
            result[name] = round(sum(scores) / len(scores), 1)
        else:
            result[name] = 0.0
    return result


# ---------------------------------------------------------------------------
# Sets  (membership, union |, intersection &, difference -, ^)
# ---------------------------------------------------------------------------

def has_duplicates(items: list) -> bool:
    """True if any value appears more than once.  Hint: compare len() with a set."""
    return len(items) != len(set(items))


def only_in_one(a: list, b: list) -> list:
    """Values in exactly ONE of the lists, sorted ascending.
    [1, 2, 3], [2, 3, 4] -> [1, 4]   Hint: symmetric difference ^."""
    return sorted(set(a) ^ set(b))


def missing_numbers(numbers: list, n: int) -> list:
    """Numbers from 1..n that are NOT in the list, sorted.
    [1, 2, 4, 6], 6 -> [3, 5]"""
    return sorted(set(range(1, n + 1)) - set(numbers))


def unique_letters(words: list) -> set:
    """All distinct lower-case letters used across the words (ignore non-letters).
    ["Hi", "ho!"] -> {"h", "i", "o"}"""
    return {ch.lower() for word in words for ch in word if ch.isalpha()}


# ---------------------------------------------------------------------------
# Comprehensions  (list / dict / set comprehensions, conditions, nesting)
# ---------------------------------------------------------------------------

def squares_of_evens(numbers: list) -> list:
    """Squares of the even numbers, as a list comprehension.  [1, 2, 3, 4] -> [4, 16]"""
    return [n * n for n in numbers if n % 2 == 0]


def word_lengths(words: list) -> dict:
    """Dict comprehension: word -> its length.  ["hi", "cat"] -> {"hi": 2, "cat": 3}"""
    return {word: len(word) for word in words}


def transpose(matrix: list) -> list:
    """Swap rows and columns.  [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]
    Empty matrix -> [].  Try a nested comprehension (or zip(*matrix))."""
    return [list(row) for row in zip(*matrix)]


def pairs_that_sum(numbers: list, target: int) -> list:
    """All (i, j) INDEX pairs with i < j where numbers[i] + numbers[j] == target.
    [1, 2, 3, 4], 5 -> [(0, 3), (1, 2)]"""
    return [(i, j)
            for i in range(len(numbers))
            for j in range(i + 1, len(numbers))
            if numbers[i] + numbers[j] == target]


# ---------------------------------------------------------------------------
# Stacks & queues  (list as a stack, collections.deque as a queue)
# ---------------------------------------------------------------------------

def is_balanced(text: str) -> bool:
    """True if (), [] and {} are correctly opened/closed and nested.
    "([]{})" -> True,  "([)]" -> False,  "((" -> False.  Ignore other characters.
    Hint: push openers onto a list, pop when you see a closer."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def last_n_items(items: list, n: int) -> list:
    """Keep only the last n items as you stream through the list.
    [1, 2, 3, 4, 5], 3 -> [3, 4, 5]   Hint: collections.deque(maxlen=n)."""
    window = deque(maxlen=n)
    for item in items:
        window.append(item)
    return list(window)


def hot_potato(names: list, k: int) -> str:
    """Players sit in a circle; pass the potato k times, then whoever holds it is out.
    Repeat until one name remains and return it.
    ["A", "B", "C", "D"], 2 -> "A"
    Hint: deque.rotate(-k) then popleft()."""
    circle = deque(names)
    while len(circle) > 1:
        circle.rotate(-k)
        circle.popleft()
    return circle[0]


# ---------------------------------------------------------------------------
# collections  (Counter, defaultdict, namedtuple)
# ---------------------------------------------------------------------------

def first_unique_char(text: str) -> int:
    """Index of the first character that appears exactly once, else -1.
    "leetcode" -> 0,  "aabb" -> -1   Hint: Counter."""
    counts = Counter(text)
    for i, ch in enumerate(text):
        if counts[ch] == 1:
            return i
    return -1


def group_anagrams(words: list) -> list:
    """Group words that are anagrams of each other. Groups and the words inside
    them keep their first-seen order.
    ["eat", "tea", "tan", "ate", "nat", "bat"]
      -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    Hint: defaultdict(list) keyed by "".join(sorted(word))."""
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


def make_point(x: float, y: float):
    """Return a namedtuple called Point with fields x and y.
    p = make_point(3, 4);  p.x -> 3,  p.y -> 4,  p == (3, 4) -> True"""
    return Point(x, y)
