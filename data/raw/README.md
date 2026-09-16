# Raw College Scorecard data

The study uses the U.S. Department of Education College Scorecard institution-level release dated June 10, 2026.

- Official data page: <https://collegescorecard.ed.gov/data/>
- Fixed archive: `Most-Recent-Cohorts-Institution_06102026.zip`
- Archive SHA-256: `f56a181b000ca4914e924c16b6b81dcc656e25aeb2ac68ab7d271ac0f29ffd58`
- Expanded CSV: `Most-Recent-Cohorts-Institution.csv`
- CSV SHA-256: `89e8a35a6588dfb81a6ce78fa9df4cb99b36ef7aa4b28fb0157f9e3e1a7d81b5`
- Data dictionary: <https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx>

The 23.6 MB compressed archive and 100.1 MB expanded CSV are intentionally omitted from the repository. Download and verify them with:

```bash
python scripts/download_scorecard_data.py
```

The script writes the files to this directory and stops if either checksum differs from the verified release.
