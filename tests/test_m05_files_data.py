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
