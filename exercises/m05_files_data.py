"""
Module 5 - Files & Data: reading/writing text, CSV and JSON. Real day-to-day work.
Use `with open(...)` and the standard csv / json modules.
"""


def count_lines(path: str) -> int:
    """Return the number of non-empty lines in a text file."""
    raise NotImplementedError


def write_report(path: str, lines: list) -> None:
    """Write each string in `lines` on its own line to `path` (overwrite the file)."""
    raise NotImplementedError


def csv_column_average(path: str, column: str) -> float:
    """CSV has a header row. Return the average of `column` as a float,
    rounded to 2 decimals. Skip rows where the value is empty or not a number.
    Raise KeyError if the column doesn't exist."""
    raise NotImplementedError


def save_json(path: str, data) -> None:
    """Save data as JSON with indent=2."""
    raise NotImplementedError


def load_json(path: str, default=None):
    """Load JSON from path. If the file doesn't exist, return `default`."""
    raise NotImplementedError


def summarize_sales(path: str) -> dict:
    """CSV columns: region,product,amount
    Return total amount per region, sorted by region name:
    {"East": 250.0, "West": 100.0}"""
    raise NotImplementedError
