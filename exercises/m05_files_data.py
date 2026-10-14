"""
Module 5 - Files & Data: reading/writing text, CSV and JSON. Real day-to-day work.
Use `with open(...)` and the standard csv / json modules.
"""
import csv
import json
from collections import Counter, deque
from pathlib import Path


def count_lines(path: str) -> int:
    """Return the number of non-empty lines in a text file."""
    with open(path) as f:
        return sum(1 for line in f if line.strip())


def write_report(path: str, lines: list) -> None:
    """Write each string in `lines` on its own line to `path` (overwrite the file)."""
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def csv_column_average(path: str, column: str) -> float:
    """CSV has a header row. Return the average of `column` as a float,
    rounded to 2 decimals. Skip rows where the value is empty or not a number.
    Raise KeyError if the column doesn't exist."""
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        if column not in reader.fieldnames:
            raise KeyError(column)
        values = []
        for row in reader:
            try:
                values.append(float(row[column]))
            except ValueError:
                continue                      # empty or not a number
    return round(sum(values) / len(values), 2)


def save_json(path: str, data) -> None:
    """Save data as JSON with indent=2."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def load_json(path: str, default=None):
    """Load JSON from path. If the file doesn't exist, return `default`."""
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def summarize_sales(path: str) -> dict:
    """CSV columns: region,product,amount
    Return total amount per region, sorted by region name:
    {"East": 250.0, "West": 100.0}"""
    totals = {}
    for row in read_csv_dicts(path):
        region = row["region"]
        totals[region] = totals.get(region, 0) + float(row["amount"])
    return dict(sorted(totals.items()))


# ---------------------------------------------------------------------------
# Text files  (read / write / append modes, iterating lines, rstrip("\n"))
# ---------------------------------------------------------------------------

def read_lines(path: str) -> list:
    """Return every line WITHOUT the trailing newline (blank lines kept).
    "a\\nb\\n\\nc\\n" -> ["a", "b", "", "c"]   Hint: f.read().splitlines()."""
    with open(path) as f:
        return f.read().splitlines()


def append_line(path: str, line: str) -> None:
    """Add `line` plus a newline to the END of the file. Create it if missing.
    Hint: open(path, "a")."""
    with open(path, "a") as f:
        f.write(line + "\n")


def count_words(path: str) -> int:
    """Total number of whitespace-separated words in the file."""
    with open(path) as f:
        return len(f.read().split())


def longest_line(path: str) -> str:
    """The longest line (without its newline). Ties: the first one. Empty file -> "" """
    return max(read_lines(path), key=len, default="")


def find_in_file(path: str, word: str) -> list:
    """Line NUMBERS (starting at 1) whose text contains `word`, case-insensitive.
    Hint: enumerate(f, start=1)."""
    word = word.lower()
    with open(path) as f:
        return [number for number, line in enumerate(f, start=1) if word in line.lower()]


def tail(path: str, n: int) -> list:
    """The last n lines (without newlines). Fewer lines than n -> all of them.
    Bonus: use collections.deque(f, maxlen=n) so big files aren't loaded fully."""
    with open(path) as f:
        last = deque(f, maxlen=n)             # only ever holds n lines in memory
    return [line.rstrip("\n") for line in last]


def replace_in_file(path: str, old: str, new: str) -> int:
    """Replace every `old` with `new` inside the file (rewrite it in place).
    Return how many replacements were made."""
    with open(path) as f:
        text = f.read()
    count = text.count(old)
    with open(path, "w") as f:
        f.write(text.replace(old, new))
    return count


def merge_files(paths: list, out_path: str) -> None:
    """Concatenate the files in order into out_path. Make sure each file's
    content ends with a newline before the next one starts."""
    with open(out_path, "w") as out:
        for p in paths:
            with open(p) as f:
                text = f.read()
            if text and not text.endswith("\n"):
                text += "\n"
            out.write(text)


# ---------------------------------------------------------------------------
# Paths & folders  (pathlib.Path, os.listdir, suffix, stat().st_size)
# ---------------------------------------------------------------------------

def change_extension(path: str, new_ext: str) -> str:
    """Return the path with a new extension (no file is touched).
    "data/report.txt", ".csv" -> "data/report.csv"   Hint: Path(path).with_suffix()."""
    return str(Path(path).with_suffix(new_ext))


def list_files_by_extension(folder: str, ext: str) -> list:
    """Sorted FILE names (not full paths) in `folder` ending in `ext`,
    case-insensitive. Ignore sub-folders.   ".txt" matches "a.TXT"."""
    ext = ext.lower()
    return sorted(
        p.name for p in Path(folder).iterdir()
        if p.is_file() and p.name.lower().endswith(ext)
    )


def folder_size(folder: str) -> int:
    """Total size in bytes of all files in folder AND its sub-folders.
    Hint: Path(folder).rglob("*") or os.walk()."""
    return sum(p.stat().st_size for p in Path(folder).rglob("*") if p.is_file())


# ---------------------------------------------------------------------------
# Parsing text  (split, partition, strip, skipping comments)
# ---------------------------------------------------------------------------

def parse_config(path: str) -> dict:
    """Read "key = value" lines into a dict of strings. Strip spaces around keys and
    values, skip blank lines and lines starting with "#". Only split on the FIRST "=".
    "url = a=b"  -> {"url": "a=b"}   Hint: str.partition("=")."""
    config = {}
    for line in read_lines(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")   # splits on the FIRST "=" only
        config[key.strip()] = value.strip()
    return config


def count_log_levels(path: str) -> dict:
    """Each line looks like "2024-01-01 12:00:00 ERROR Something broke".
    The level is the 3rd word. Return {level: count}, keys sorted alphabetically.
    Skip lines with fewer than 3 words."""
    counts = Counter()
    for line in read_lines(path):
        parts = line.split()
        if len(parts) >= 3:
            counts[parts[2]] += 1
    return dict(sorted(counts.items()))


# ---------------------------------------------------------------------------
# CSV  (csv.DictReader / csv.DictWriter, newline="", converting types)
# ---------------------------------------------------------------------------

def read_csv_dicts(path: str) -> list:
    """Return the rows as a list of dicts (all values stay strings).
    Hint: list(csv.DictReader(f))."""
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: str, rows: list) -> None:
    """Write a list of dicts to CSV with a header row. Column order = keys of
    the first row. Empty list -> create an empty file.
    Hint: csv.DictWriter, open(path, "w", newline="")."""
    with open(path, "w", newline="") as f:
        if not rows:
            return
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def filter_csv(in_path: str, out_path: str, column: str, value: str) -> int:
    """Copy only the rows where row[column] == value (header included).
    Return the number of data rows written."""
    with open(in_path, newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        matches = [row for row in reader if row[column] == value]
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(matches)
    return len(matches)


def top_n_rows(path: str, column: str, n: int) -> list:
    """The n rows (as dicts) with the largest NUMERIC value in `column`, biggest first."""
    rows = read_csv_dicts(path)
    rows.sort(key=lambda row: float(row[column]), reverse=True)   # numeric, not text
    return rows[:n]


def clean_csv(in_path: str, out_path: str) -> int:
    """Write a cleaned copy: strip spaces from every value, drop rows that have
    any empty value, and drop exact duplicate rows (keep the first).
    Return the number of data rows kept."""
    with open(in_path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        seen = set()
        kept = []
        for row in reader:
            row = tuple(value.strip() for value in row)
            if all(row) and row not in seen:          # no empty values, not a duplicate
                seen.add(row)
                kept.append(row)
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(kept)
    return len(kept)


# ---------------------------------------------------------------------------
# JSON  (json.load / json.dump, nested data, JSON Lines)
# ---------------------------------------------------------------------------

def update_json(path: str, key: str, value) -> dict:
    """Load the JSON object at path (or {} if the file is missing), set key = value,
    save it back and return the updated dict."""
    data = load_json(path, default={})
    data[key] = value
    save_json(path, data)
    return data


def flatten_json(data: dict, sep: str = ".") -> dict:
    """Flatten nested dicts into one level, joining keys with sep.
    {"a": {"b": 1, "c": {"d": 2}}, "e": 3} -> {"a.b": 1, "a.c.d": 2, "e": 3}
    Lists and other values are left as they are.   Hint: recursion."""
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for inner_key, inner_value in flatten_json(value, sep).items():
                flat[key + sep + inner_key] = inner_value
        else:
            flat[key] = value
    return flat


def csv_to_json(csv_path: str, json_path: str) -> int:
    """Convert a CSV file into a JSON list of objects (values stay strings).
    Return the number of records."""
    records = read_csv_dicts(csv_path)
    save_json(json_path, records)
    return len(records)


def write_jsonl(path: str, records: list) -> None:
    """JSON Lines: write each record as compact JSON on its own line."""
    with open(path, "w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")


def read_jsonl(path: str) -> list:
    """Read a JSON Lines file back into a list. Skip blank lines."""
    return [json.loads(line) for line in read_lines(path) if line.strip()]


def count_by_field(path: str, field: str) -> dict:
    """The file holds a JSON list of objects. Count records per value of `field`;
    records without the field are counted under "unknown".
    [{"dept": "IT"}, {"dept": "HR"}, {"dept": "IT"}, {}] -> {"IT": 2, "HR": 1, "unknown": 1}"""
    counts = Counter(record.get(field, "unknown") for record in load_json(path))
    return dict(counts)
