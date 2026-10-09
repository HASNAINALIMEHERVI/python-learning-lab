# Python File Utilities

Personal learning utilities by Hasnain Ali Mehervi, substantially repaired from supplied `table.py` and `new.py`. No paid-client claim.

Requires Python 3.10+; the chart exporter also requires `pip install -r requirements.txt`.

```sh
python tables.py --start 1 --end 20 --rows 10 --output generated-tables
python csv_chart.py sample.csv scores.xlsx
python -m unittest discover -s tests -v
```

The table generator writes every row once, creates the selected directory and refuses existing outputs. The Excel exporter reads name/score columns, derives chart ranges from actual records and refuses to overwrite an existing file. Names are stored as text, including names starting with `=`, to avoid accidental spreadsheet formulas. Other input columns are deliberately not exported.

`sample.csv` contains newly invented demo labels, not the uploaded names, ages or locations. Use only data you are authorized to process. Output creation is exclusive, but an I/O failure during export can leave a partial new file; inspect it before use. Tests validate saved chart ranges and text cell types; Excel desktop visual rendering has not been checked.
