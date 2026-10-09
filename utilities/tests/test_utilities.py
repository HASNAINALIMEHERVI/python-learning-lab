import tempfile
import unittest
from pathlib import Path
from openpyxl import load_workbook
from tables import generate
from csv_chart import convert


class UtilitiesTests(unittest.TestCase):
    def test_all_table_rows_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            targets = generate(2, 3, 10, folder)
            self.assertEqual(len(targets), 2)
            self.assertEqual(targets[0].read_text().splitlines()[-1], '2 × 10 = 20')
            self.assertEqual(len(targets[0].read_text().splitlines()), 10)
            with self.assertRaises(FileExistsError):
                generate(2, 3, 10, folder)

    def test_export_ranges_text_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/'input.csv', Path(folder)/'output.xlsx'
            source.write_text('name,score\n=1+1,5\nDemo,9\n')
            self.assertEqual(convert(source, output), 2)
            workbook = load_workbook(output)
            sheet = workbook.active
            self.assertEqual(sheet['A2'].value, '=1+1')
            self.assertEqual(sheet['A2'].data_type, 's')
            self.assertEqual(sheet._charts[0].series[0].val.numRef.f, "'Scores'!$B$2:$B$3")
            workbook.close()
            original = output.read_bytes()
            with self.assertRaises(FileExistsError):
                convert(source, output)
            self.assertEqual(output.read_bytes(), original)

    def test_invalid_inputs_leave_no_output(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/'input.csv', Path(folder)/'output.xlsx'
            for content in ['name,score\n', 'name,score\nDemo,nan\n', 'wrong,score\nDemo,5\n']:
                source.write_text(content)
                with self.assertRaises(ValueError):
                    convert(source, output)
                self.assertFalse(output.exists())
            with self.assertRaises(ValueError):
                generate(0, 3, 10, folder)
