import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
json_path = root / "data" / "bibliography.json"
csv_path = root / "data" / "bibliography.csv"
time_path = root / "data" / "timeline.csv"

rows = json.loads(json_path.read_text())

fields = [
    "id","title","type","date","organization","url","tier",
    "relevance_tags","why_it_matters","open_source","reproducible","industrial_value","notes"
]

with csv_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for r in rows:
        rr = dict(r)
        rr["relevance_tags"] = ";".join(r.get("relevance_tags", []))
        w.writerow(rr)

with time_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["date","id","title","type","organization","tier","url"])
    w.writeheader()
    for r in sorted(rows, key=lambda x: x.get("date", "")):
        w.writerow({k:r.get(k,"") for k in ["date","id","title","type","organization","tier","url"]})

print(f"wrote {csv_path} and {time_path}")
