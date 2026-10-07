"""
Check your progress and generate a report you can show your manager.

    python check_progress.py                 # run all modules
    python check_progress.py -m 3            # run only module 3 (detailed output)
    python check_progress.py --note "Finished OOP module"

Every full run is saved to progress_history.json and progress_report.html
is regenerated, so the report shows your improvement over time.
"""
import argparse
import datetime as dt
import html
import io
import json
import os
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))
HISTORY = os.path.join(ROOT, "progress_history.json")
REPORT = os.path.join(ROOT, "progress_report.html")

MODULES = [
    ("m01_basics", "1. Basics"),
    ("m02_data_structures", "2. Data Structures"),
    ("m03_functions_errors", "3. Functions & Errors"),
    ("m04_oop", "4. OOP"),
    ("m05_files_data", "5. Files & Data"),
    ("m06_algorithms", "6. Algorithms"),
]


def run_module(mod):
    suite = unittest.defaultTestLoader.loadTestsFromName(f"tests.test_{mod}")
    names = [t.id().split(".")[-1].replace("test_", "") for t in _iter(suite)]
    result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    failed = {}
    for test, tb in result.failures + result.errors:
        name = test.id().split(".")[-1].replace("test_", "")
        last = tb.strip().splitlines()[-1]
        failed[name] = "not started" if "NotImplementedError" in last else last
    return {"total": len(names), "passed": len(names) - len(failed),
            "results": {n: failed.get(n, "passed") for n in names}}


def _iter(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from _iter(item)
        else:
            yield item


def load_history():
    try:
        with open(HISTORY) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def print_module(label, r, detailed):
    pct = 100 * r["passed"] // r["total"]
    bar = "#" * (pct // 5) + "-" * (20 - pct // 5)
    print(f"{label:<24} [{bar}] {r['passed']:>2}/{r['total']}  {pct:>3}%")
    if detailed:
        for name, status in r["results"].items():
            mark = "PASS" if status == "passed" else "TODO" if status == "not started" else "FAIL"
            extra = "" if mark != "FAIL" else f"  -> {status}"
            print(f"    [{mark}] {name}{extra}")


def write_report(history):
    latest = history[-1]
    rows_mod = ""
    for mod, label in MODULES:
        r = latest["modules"][mod]
        pct = 100 * r["passed"] / r["total"]
        rows_mod += (f"<tr><td>{label}</td><td>{r['passed']}/{r['total']}</td>"
                     f"<td><div class='bar'><span style='width:{pct:.0f}%'></span></div></td>"
                     f"<td>{pct:.0f}%</td></tr>")
    rows_hist = ""
    for h in reversed(history):
        rows_hist += (f"<tr><td>{h['timestamp']}</td><td>{h['passed']}/{h['total']}</td>"
                      f"<td>{h['percent']}%</td><td>{html.escape(h.get('note', ''))}</td></tr>")
    first = history[0]
    days = (dt.datetime.fromisoformat(latest["timestamp"]) -
            dt.datetime.fromisoformat(first["timestamp"])).days
    points = " ".join(
        f"{40 + i * (520 / max(len(history) - 1, 1)):.0f},{180 - h['percent'] * 1.6:.0f}"
        for i, h in enumerate(history))
    page = f"""<!doctype html><html><head><meta charset="utf-8">
<title>Python Practice Progress</title><style>
body{{font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:30px auto;padding:0 16px;color:#222}}
h1{{margin-bottom:4px}} .muted{{color:#666}}
.cards{{display:flex;gap:12px;margin:20px 0;flex-wrap:wrap}}
.card{{flex:1;min-width:150px;background:#f4f6fb;border-radius:10px;padding:14px}}
.card b{{font-size:28px;display:block}}
table{{width:100%;border-collapse:collapse;margin:10px 0 28px}}
td,th{{padding:8px;border-bottom:1px solid #e5e5e5;text-align:left}}
.bar{{background:#e6e9f2;border-radius:6px;height:12px;width:220px}}
.bar span{{display:block;height:100%;background:#3a7bd5;border-radius:6px}}
</style></head><body>
<h1>Python Practice Progress Report</h1>
<div class="muted">Generated {latest['timestamp']} &middot; {len(history)} check-ins over {days} day(s)</div>
<div class="cards">
<div class="card">Overall<b>{latest['percent']}%</b></div>
<div class="card">Exercises passed<b>{latest['passed']}/{latest['total']}</b></div>
<div class="card">Improvement since start<b>+{latest['percent'] - first['percent']}%</b></div>
</div>
<h2>Progress over time</h2>
<svg viewBox="0 0 580 200" width="100%" style="max-width:580px">
<line x1="40" y1="180" x2="560" y2="180" stroke="#bbb"/><line x1="40" y1="20" x2="40" y2="180" stroke="#bbb"/>
<text x="5" y="24" font-size="11">100%</text><text x="15" y="183" font-size="11">0%</text>
<polyline points="{points}" fill="none" stroke="#3a7bd5" stroke-width="3"/></svg>
<h2>By module</h2><table><tr><th>Module</th><th>Passed</th><th></th><th>%</th></tr>{rows_mod}</table>
<h2>Check-in log</h2><table><tr><th>Date</th><th>Passed</th><th>%</th><th>Note</th></tr>{rows_hist}</table>
</body></html>"""
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(page)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-m", "--module", type=int, help="run one module (1-6) with details")
    p.add_argument("--note", default="", help="note to save with this check-in")
    args = p.parse_args()
    os.chdir(ROOT)

    if args.module:
        mod, label = MODULES[args.module - 1]
        print_module(label, run_module(mod), detailed=True)
        return

    modules = {}
    print("\nPython Practice - Progress Check\n" + "=" * 52)
    for mod, label in MODULES:
        modules[mod] = run_module(mod)
        print_module(label, modules[mod], detailed=False)
    passed = sum(r["passed"] for r in modules.values())
    total = sum(r["total"] for r in modules.values())
    pct = round(100 * passed / total)
    print("=" * 52 + f"\nOVERALL: {passed}/{total} ({pct}%)")

    history = load_history()
    history.append({"timestamp": dt.datetime.now().isoformat(timespec="minutes"),
                    "passed": passed, "total": total, "percent": pct,
                    "note": args.note, "modules": modules})
    with open(HISTORY, "w") as f:
        json.dump(history, f, indent=2)
    write_report(history)
    print(f"\nReport updated: {REPORT}")
    print("Tip: run with -m <number> to see which exercises are left in a module.\n")


if __name__ == "__main__":
    main()
