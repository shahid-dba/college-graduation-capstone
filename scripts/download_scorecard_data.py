#!/usr/bin/env python3
"""Download and verify the fixed College Scorecard release used by the project."""

from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
ARCHIVE_NAME = "Most-Recent-Cohorts-Institution_06102026.zip"
CSV_NAME = "Most-Recent-Cohorts-Institution.csv"
ARCHIVE_URL = (
    "https://ed-public-download.scorecard.network/downloads/"
    "Most-Recent-Cohorts-Institution_06102026.zip"
)
DICTIONARY_URL = (
    "https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx"
)
ARCHIVE_SHA256 = "f56a181b000ca4914e924c16b6b81dcc656e25aeb2ac68ab7d271ac0f29ffd58"
CSV_SHA256 = "89e8a35a6588dfb81a6ce78fa9df4cb99b36ef7aa4b28fb0157f9e3e1a7d81b5"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path) -> None:
    temporary = destination.with_suffix(destination.suffix + ".part")
    with requests.get(url, stream=True, timeout=120) as response:
        response.raise_for_status()
        with temporary.open("wb") as stream:
            shutil.copyfileobj(response.raw, stream)
    temporary.replace(destination)


def verify(path: Path, expected: str) -> None:
    observed = sha256(path)
    if observed != expected:
        raise RuntimeError(
            f"Checksum mismatch for {path.name}: expected {expected}, observed {observed}"
        )


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    archive = RAW_DIR / ARCHIVE_NAME
    csv_path = RAW_DIR / CSV_NAME
    dictionary = RAW_DIR / "CollegeScorecardDataDictionary.xlsx"

    if not archive.exists():
        print(f"Downloading {ARCHIVE_NAME}")
        download(ARCHIVE_URL, archive)
    verify(archive, ARCHIVE_SHA256)

    if not csv_path.exists():
        print(f"Extracting {CSV_NAME}")
        with zipfile.ZipFile(archive) as bundle:
            source_name = next(
                name for name in bundle.namelist() if Path(name).name == CSV_NAME
            )
            with bundle.open(source_name) as source, csv_path.open("wb") as target:
                shutil.copyfileobj(source, target)
    verify(csv_path, CSV_SHA256)

    if not dictionary.exists():
        print("Downloading the College Scorecard data dictionary")
        download(DICTIONARY_URL, dictionary)

    manifest = {
        "official_data_page": "https://collegescorecard.ed.gov/data/",
        "resolved_download_url": ARCHIVE_URL,
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_filename": archive.name,
        "source_size_bytes": archive.stat().st_size,
        "source_sha256": sha256(archive),
        "csv_filename": csv_path.name,
        "csv_size_bytes": csv_path.stat().st_size,
        "csv_sha256": sha256(csv_path),
        "dictionary_filename": dictionary.name,
        "dictionary_url": DICTIONARY_URL,
    }
    (RAW_DIR / "source_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print("Source files downloaded and verified successfully.")


if __name__ == "__main__":
    main()
