#!/usr/bin/env python3
"""
ColumnForge
-----------
Batch-extract spreadsheet columns into .txt files.

Point this at a folder, and for every .xlsx file inside, it creates a
matching "output-<filename>" folder (in that same folder) containing one
.txt file per column. The column header becomes the filename, and each
row's value in that column becomes one line in the file.

Usage:
    python columnforge.py <folder> [--sheet SHEET_NAME]

Example:
    python columnforge.py ./spreadsheets
    python columnforge.py ./spreadsheets --sheet "Sheet2"
"""
import re
import argparse
from pathlib import Path
import pandas as pd

__version__ = "1.0.0"


def sanitize_filename(name: str) -> str:
    name = str(name).strip()
    name = re.sub(r'[\\/*?:"<>|]', "_", name)  # remove illegal filename chars
    name = re.sub(r'\s+', "_", name)
    return name or "unnamed_column"


def extract_one(xlsx_path: Path, sheet):
    """Extract all columns of one spreadsheet into its own output-<name> folder."""
    out_dir = xlsx_path.parent / f"output-{xlsx_path.stem}"
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_excel(xlsx_path, sheet_name=sheet, dtype=str)

    used_names = {}
    for col in df.columns:
        base_name = sanitize_filename(col)
        count = used_names.get(base_name, 0)
        used_names[base_name] = count + 1
        filename = base_name if count == 0 else f"{base_name}_{count}"

        values = df[col].fillna("").tolist()
        file_path = out_dir / f"{filename}.txt"
        file_path.write_text("\n".join(values), encoding="utf-8")

    print(f"  -> {len(df.columns)} column(s) written to '{out_dir}/'")


def main():
    parser = argparse.ArgumentParser(
        prog="columnforge",
        description="ColumnForge — batch-extract spreadsheet columns into .txt files."
    )
    parser.add_argument("folder", help="Folder containing .xlsx file(s) to process")
    parser.add_argument("--sheet", default=0, help="Sheet name or index to read (default: first sheet)")
    parser.add_argument("--version", action="version", version=f"ColumnForge {__version__}")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a folder.")
        return

    sheet = args.sheet
    if isinstance(sheet, str) and sheet.isdigit():
        sheet = int(sheet)

    xlsx_files = sorted(folder.glob("*.xlsx"))
    # Skip Excel's own temp/lock files (start with ~$)
    xlsx_files = [f for f in xlsx_files if not f.name.startswith("~$")]

    if not xlsx_files:
        print(f"No .xlsx files found in '{folder}'.")
        return

    print(f"ColumnForge: found {len(xlsx_files)} spreadsheet(s) in '{folder}'\n")

    for xlsx_path in xlsx_files:
        print(f"Processing '{xlsx_path.name}'...")
        try:
            extract_one(xlsx_path, sheet)
        except Exception as e:
            print(f"  !! Failed: {e}")

    print(f"\nDone. Processed {len(xlsx_files)} spreadsheet(s).")


if __name__ == "__main__":
    main()
