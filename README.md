# Python Practice Modules — with Progress Tracking

6 modules, 168 exercises. No installs needed (only Python 3.8+ standard library).

| Module | Topics |
|---|---|
| 1. Basics | numbers & arithmetic, type conversion, strings, conditions, loops |
| 2. Data Structures | lists, tuples, dicts, sets, comprehensions, stacks & queues, collections (Counter, defaultdict, deque, namedtuple) |
| 3. Functions & Errors | defaults, *args/**kwargs, lambdas, closures, recursion, exceptions, decorators, generators |
| 4. OOP | classes, properties, class/static methods, inheritance, ABCs & mixins, dunder methods, iterators, context managers, dataclasses, composition |
| 5. Files & Data | text files, paths & folders (pathlib), parsing config/log files, CSV, JSON, JSON Lines |
| 6. Algorithms | searching, stacks, hashing, efficiency |

## How to use
1. Open a file in `exercises/` and replace each `raise NotImplementedError` with your code.
2. From this folder, run:
   ```
   python check_progress.py                  # check everything + update report
   python check_progress.py -m 2             # see which exercises in module 2 pass/fail
   python check_progress.py --note "Finished module 3"
   ```
3. Open `progress_report.html` in a browser — it shows your overall score, per-module
   progress, a chart over time, and a dated log of every check-in.

## Tips for the PIP
- Do a first check-in today (0% is fine — it's your baseline).
- Check in after every session with a short `--note`. A steady upward line with dates
  is strong evidence of consistent effort.
- Don't edit the files in `tests/` — those are the "proof" your code works.
- Commit your work to Git as you go; commit history is another record of progress.
