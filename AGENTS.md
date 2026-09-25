# Repository Guidelines & Agent Instructions

## 🚨 Mandatory Pre-Push Rule: Always Synchronize README Progress

Whenever changes (such as solved exercises, notebook executions, or code updates) are to be committed and pushed to GitHub:

1. **Analyze Notebook Progress**:
   - Scan all notebooks in `notebooks/` to detect all completed exercise cells and get an accurate count of solved exercises out of 100.

2. **Update [README.md](file:///d:/My%20Codings/numpy-100-exercises-solutions/README.md)**:
   - **Progress Badge**: Update `[![Progress](https://img.shields.io/badge/Progress-<COUNT>%20%2F%20100%20Solved-38BDF8?style=for-the-badge)](notebooks/)`.
   - **ASCII Progress Bar**: Update the block diagram and percentage:
     ```text
     Current Progress: [<BLOCKS>] <COUNT> / 100 Solved (<PERCENT>%)
     ```
   - **The 7 Practice Notebooks Table**: Update the `Status` column for any notebooks whose exercises were modified/completed.
   - **Master Progress Tracker & Checklist**: Check off all newly completed exercises with `[x]`.

3. **Stage, Commit, and Push Together**:
   - Always stage the updated `README.md` alongside the notebook changes so that the remote repository on GitHub always stays in sync with actual progress.
