#!/usr/bin/env python3
import json
from pathlib import Path


def main():
    input_path = Path("deck.json")
    output_path = Path("deck-stripped.json")

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "notes" in data:
        data["notes"] = []

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
