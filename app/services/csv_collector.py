import csv
from pathlib import Path


DATA_DIR = Path("data")


def import_csv(filename: str) -> int:
    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {filename}")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    return len(rows)
