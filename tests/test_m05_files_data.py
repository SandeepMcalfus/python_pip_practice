import os
import tempfile
import unittest
from exercises import m05_files_data as m


class TestFilesData(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def path(self, name, content=None):
        p = os.path.join(self.dir, name)
        if content is not None:
            with open(p, "w", newline="") as f:
                f.write(content)
        return p

    def test_count_lines(self):
        p = self.path("a.txt", "one\n\ntwo\n   \nthree\n")
        self.assertEqual(m.count_lines(p), 3)

    def test_write_report(self):
        p = self.path("r.txt")
        m.write_report(p, ["a", "b"])
        with open(p) as f:
            self.assertEqual(f.read().splitlines(), ["a", "b"])

    def test_csv_column_average(self):
        p = self.path("d.csv", "name,score\nA,10\nB,\nC,abc\nD,25\n")
        self.assertEqual(m.csv_column_average(p, "score"), 17.5)
        with self.assertRaises(KeyError):
            m.csv_column_average(p, "missing")

    def test_json_roundtrip(self):
        p = self.path("d.json")
        m.save_json(p, {"x": [1, 2]})
        self.assertEqual(m.load_json(p), {"x": [1, 2]})
        self.assertEqual(m.load_json(self.path("nope.json"), default={}), {})

    def test_summarize_sales(self):
        p = self.path("s.csv", "region,product,amount\nWest,pen,100\nEast,ink,200\nEast,pen,50\n")
        result = m.summarize_sales(p)
        self.assertEqual(result, {"East": 250.0, "West": 100.0})
        self.assertEqual(list(result), ["East", "West"])

    def read(self, p):
        with open(p, newline="") as f:
            return f.read()

    # --- Text files -------------------------------------------------------

    def test_read_lines(self):
        p = self.path("a.txt", "a\nb\n\nc\n")
        self.assertEqual(m.read_lines(p), ["a", "b", "", "c"])

    def test_append_line(self):
        p = self.path("log.txt")
        m.append_line(p, "first")
        m.append_line(p, "second")
        self.assertEqual(self.read(p), "first\nsecond\n")

    def test_count_words(self):
        p = self.path("w.txt", "the quick  brown\n\nfox jumps\n")
        self.assertEqual(m.count_words(p), 5)
        self.assertEqual(m.count_words(self.path("e.txt", "")), 0)

    def test_longest_line(self):
        p = self.path("l.txt", "hi\nhello\nworld\n")
        self.assertEqual(m.longest_line(p), "hello")
        self.assertEqual(m.longest_line(self.path("e.txt", "")), "")

    def test_find_in_file(self):
        p = self.path("f.txt", "Python is fun\nJava\nI like PYTHON\n")
        self.assertEqual(m.find_in_file(p, "python"), [1, 3])
        self.assertEqual(m.find_in_file(p, "rust"), [])

    def test_tail(self):
        p = self.path("t.txt", "1\n2\n3\n4\n5\n")
        self.assertEqual(m.tail(p, 2), ["4", "5"])
        self.assertEqual(m.tail(p, 10), ["1", "2", "3", "4", "5"])

    def test_replace_in_file(self):
        p = self.path("r.txt", "cat and cat\nno cats here? cat\n")
        self.assertEqual(m.replace_in_file(p, "cat", "dog"), 4)
        self.assertEqual(self.read(p), "dog and dog\nno dogs here? dog\n")
        self.assertEqual(m.replace_in_file(p, "zebra", "x"), 0)

    def test_merge_files(self):
        a = self.path("a.txt", "one\n")
        b = self.path("b.txt", "two")
        c = self.path("c.txt", "three\n")
        out = self.path("out.txt")
        m.merge_files([a, b, c], out)
        self.assertEqual(self.read(out), "one\ntwo\nthree\n")

    # --- Paths & folders --------------------------------------------------

    def test_change_extension(self):
        self.assertEqual(m.change_extension("data/report.txt", ".csv"),
                         os.path.join("data", "report.csv"))
        self.assertEqual(m.change_extension("notes", ".md"), "notes.md")

    def test_list_files_by_extension(self):
        self.path("b.txt", "x")
        self.path("a.TXT", "x")
        self.path("c.csv", "x")
        os.mkdir(os.path.join(self.dir, "folder.txt"))
        self.assertEqual(m.list_files_by_extension(self.dir, ".txt"), ["a.TXT", "b.txt"])
        self.assertEqual(m.list_files_by_extension(self.dir, ".json"), [])

    def test_folder_size(self):
        self.path("a.txt", "12345")
        sub = os.path.join(self.dir, "sub")
        os.mkdir(sub)
        with open(os.path.join(sub, "b.txt"), "w", newline="") as f:
            f.write("123")
        self.assertEqual(m.folder_size(self.dir), 8)

    # --- Parsing text -----------------------------------------------------

    def test_parse_config(self):
        p = self.path("app.cfg", "# settings\nhost = localhost\n\nport=8080\nurl = a=b\n  # indented comment\n")
        self.assertEqual(m.parse_config(p),
                         {"host": "localhost", "port": "8080", "url": "a=b"})

    def test_count_log_levels(self):
        p = self.path("app.log",
                      "2024-01-01 10:00:00 INFO started\n"
                      "2024-01-01 10:00:01 ERROR boom\n"
                      "bad line\n"
                      "2024-01-01 10:00:02 INFO ok\n"
                      "2024-01-01 10:00:03 WARNING hmm\n")
        result = m.count_log_levels(p)
        self.assertEqual(result, {"ERROR": 1, "INFO": 2, "WARNING": 1})
        self.assertEqual(list(result), ["ERROR", "INFO", "WARNING"])

    # --- CSV --------------------------------------------------------------

    def test_read_csv_dicts(self):
        p = self.path("p.csv", "name,age\nAna,30\nBo,25\n")
        self.assertEqual(m.read_csv_dicts(p),
                         [{"name": "Ana", "age": "30"}, {"name": "Bo", "age": "25"}])

    def test_write_csv(self):
        p = self.path("o.csv")
        m.write_csv(p, [{"name": "Ana", "age": 30}, {"name": "Bo", "age": 25}])
        self.assertEqual(self.read(p).splitlines(), ["name,age", "Ana,30", "Bo,25"])
        e = self.path("empty.csv")
        m.write_csv(e, [])
        self.assertEqual(self.read(e), "")

    def test_filter_csv(self):
        src = self.path("s.csv", "name,dept\nAna,IT\nBo,HR\nCy,IT\n")
        out = self.path("it.csv")
        self.assertEqual(m.filter_csv(src, out, "dept", "IT"), 2)
        self.assertEqual(self.read(out).splitlines(), ["name,dept", "Ana,IT", "Cy,IT"])

    def test_top_n_rows(self):
        p = self.path("s.csv", "name,score\nAna,9\nBo,80\nCy,75\nDi,100\n")
        self.assertEqual([r["name"] for r in m.top_n_rows(p, "score", 2)], ["Di", "Bo"])

    def test_clean_csv(self):
        src = self.path("dirty.csv",
                        "name,city\n Ana , Pune\nBo,\nAna,Pune\nCy,Delhi\n")
        out = self.path("clean.csv")
        self.assertEqual(m.clean_csv(src, out), 2)
        self.assertEqual(self.read(out).splitlines(), ["name,city", "Ana,Pune", "Cy,Delhi"])

    # --- JSON -------------------------------------------------------------

    def test_update_json(self):
        p = self.path("cfg.json")
        self.assertEqual(m.update_json(p, "theme", "dark"), {"theme": "dark"})
        self.assertEqual(m.update_json(p, "size", 12), {"theme": "dark", "size": 12})
        self.assertEqual(m.load_json(p), {"theme": "dark", "size": 12})

    def test_flatten_json(self):
        self.assertEqual(m.flatten_json({"a": {"b": 1, "c": {"d": 2}}, "e": 3}),
                         {"a.b": 1, "a.c.d": 2, "e": 3})
        self.assertEqual(m.flatten_json({"a": {"b": [1, 2]}}, sep="_"), {"a_b": [1, 2]})
        self.assertEqual(m.flatten_json({}), {})

    def test_csv_to_json(self):
        src = self.path("p.csv", "name,age\nAna,30\nBo,25\n")
        out = self.path("p.json")
        self.assertEqual(m.csv_to_json(src, out), 2)
        self.assertEqual(m.load_json(out),
                         [{"name": "Ana", "age": "30"}, {"name": "Bo", "age": "25"}])

    def test_jsonl_roundtrip(self):
        p = self.path("d.jsonl")
        records = [{"id": 1, "tags": ["a"]}, {"id": 2, "tags": []}]
        m.write_jsonl(p, records)
        self.assertEqual(len(self.read(p).splitlines()), 2)
        self.assertEqual(m.read_jsonl(p), records)
        q = self.path("gaps.jsonl", '{"a": 1}\n\n{"a": 2}\n')
        self.assertEqual(m.read_jsonl(q), [{"a": 1}, {"a": 2}])

    def test_count_by_field(self):
        p = self.path("e.json", '[{"dept": "IT"}, {"dept": "HR"}, {"dept": "IT"}, {}]')
        self.assertEqual(m.count_by_field(p, "dept"), {"IT": 2, "HR": 1, "unknown": 1})
