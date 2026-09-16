# GitHub upload guide

Target repository: <https://github.com/shahid-dba/college-graduation-capstone>

## Recommended method: GitHub website

1. Download and extract `college-graduation-capstone-github-ready.zip`.
2. Open the target repository and select **Add file**, then **Upload files**.
3. Open the extracted `college-graduation-capstone` folder and drag all of its contents into the upload area. Upload the contents, not the outer folder itself.
4. Confirm that the browser shows the root files and folders listed below.
5. Enter the commit message `Add complete reproducible capstone project`.
6. Commit directly to `main`, or create a branch if your course requires review.
7. Open the repository after the upload and verify that the notebook renders, the report PDF opens, and the folder structure is intact.
8. Create a GitHub Release named `QM640 Capstone Final Outputs` and attach the separately supplied `QM640_Capstone_Outputs.zip`. Do not add that archive to the main repository because `.gitignore` intentionally excludes it.

## Upload order and checklist

The website accepts one drag-and-drop batch. If you prefer smaller batches, use this order:

1. Root documentation: `README.md`, `LICENSE`, `.gitignore`, `requirements_locked.txt`, and `GITHUB_UPLOAD_GUIDE.md`.
2. Notebook: `notebooks/QM640_College_Graduation_Fully_Executed_Shahid_Ahmad.ipynb`.
3. Data documentation and processed data: `data/`.
4. Reproducibility script: `scripts/`.
5. Model artifacts: `models/`.
6. Tables and figures: `reports/tables/` and `reports/figures/`.
7. Final report and automated summary: `reports/final/` and `reports/automated_results_summary.md`.
8. Optional presentation: `docs/QM640_Capstone_Final_Presentation_Shahid_Ahmad.pdf`.
9. Integrity record: `checksums.sha256`.
10. GitHub Release asset: upload `QM640_Capstone_Outputs.zip` on the repository's **Releases** page, not as a tracked repository file.

## Command-line alternative

Run these commands inside the extracted `college-graduation-capstone` folder:

```bash
git init
git branch -M main
git add .
git commit -m "Add complete reproducible capstone project"
git remote add origin https://github.com/shahid-dba/college-graduation-capstone.git
git push -u origin main
```

If the GitHub repository already contains commits, clone it first and copy these files into the clone. Do not force-push or overwrite existing history.

## Files that must remain outside Git history

Do not commit the raw archive, expanded raw CSV, downloaded Excel dictionary, virtual environment, LaTeX build products, or notebook checkpoint folders. The supplied `.gitignore` blocks these files.
