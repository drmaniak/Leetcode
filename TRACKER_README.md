# LeetCode Problem Tracker

## Overview

This repository includes a CSV-based tracking system for LeetCode problems you've solved. The tracker automatically logs successful problem solves and helps you monitor your progress, track solving patterns, and identify areas for improvement.

## Files

- `leetcode_tracker.csv` - Main tracking spreadsheet
- `solve.py` - Interactive script for logging solve attempts
- `generate_tracker.py` - Script to regenerate the tracker from your code files
- `TRACKER_README.md` - This documentation
- `.tracker_backups/` - Automatic CSV backups (created when using solve.py)

## CSV Schema

The tracker includes the following columns:

| Column                | Description                                           |
| --------------------- | ----------------------------------------------------- |
| **Problem Name**      | Human-readable problem name (e.g., "Two Sum")         |
| **Problem Number**    | Official LeetCode problem number (e.g., 1, 206, 875)  |
| **LeetCode URL**      | Direct link to the problem on LeetCode                |
| **Topics**            | Problem categories (Array, Stack, Two Pointers, etc.) |
| **First Solved Date** | Date when you first solved the problem                |
| **Last Solved Date**  | Most recent date you solved the problem               |
| **Times Solved**      | Counter for number of solving attempts                |
| **Difficulty**        | Easy/Medium/Hard (manually fill this in)              |
| **Notes**             | Personal notes about the problem or solution          |

## Usage

### Streamlined Workflow (Recommended)

Use the `solve.py` script to automatically track when you work on problems:

```bash
# Quick logging (default)
python3 solve.py Arrays/valid_sudoku.py

# Interactive mode with prompts
python3 solve.py Arrays/valid_sudoku.py --notes

# View tracker status and recent activity
python3 solve.py --status
```

**How it works:**
1. **Executes your problem file** with a 30-second timeout
2. **Only tracks on success** - if tests pass (exit code 0)
3. **Auto-detects new problems** and adds them to the tracker
4. **Increments solve counter** for existing problems
5. **Creates automatic backups** before any changes

**Smart Features:**
- ✅ New problems are automatically added to tracker
- ✅ Failed executions don't affect your tracking data
- ✅ Categorizes problems by directory (Arrays, Stacks, etc.)
- ✅ Generates LeetCode URLs based on filename
- ✅ Creates timestamped backups in `.tracker_backups/`

### Alternative: Manual Tracker Generation (Legacy)

If you prefer the old workflow or need to bulk-add problems:

```bash
python3 generate_tracker.py
```

This will scan all `.py` files and update the CSV with any new problems. However, the streamlined `solve.py` workflow is now recommended for regular use.

### Manual Updates (Optional)

You can still manually edit the CSV for:

- **Difficulty**: Add Easy/Medium/Hard based on LeetCode's rating
- **Notes**: Add detailed observations or approach notes

## Problem Mapping

The generator automatically maps common problem filenames to their LeetCode numbers. Currently mapped problems include:

- Two Sum (1)
- Valid Parentheses (20)
- Remove Duplicates in Sorted Array (26)
- Climbing Stairs (70)
- Valid Palindrome (125)
- Two Sum II - Input Array Is Sorted (167)
- Best Time to Buy and Sell Stock (121)
- And many more...

For unmapped problems, the LeetCode URL is generated based on the filename, but you may need to manually verify the links.

## Analysis Ideas

Use the CSV data for:

- **Progress tracking**: Count problems solved over time
- **Pattern analysis**: Identify which topics you solve most/least
- **Retention tracking**: Monitor how often you re-solve problems
- **Difficulty progression**: Track your advancement through difficulty levels

## Customization

To add more problem mappings, edit the `PROBLEM_MAPPINGS` dictionary in `generate_tracker.py`:

```python
PROBLEM_MAPPINGS = {
    'your_filename': leetcode_problem_number,
    # Add more mappings here
}
```

Then regenerate the CSV to apply the changes.

## CSV Import

The CSV can be imported into:

- Excel/Google Sheets for advanced analysis and charts
- Python pandas for data analysis
- Any spreadsheet application for manual tracking

## Tips

- Keep the CSV updated as you solve new problems
- Use the Notes column to track different approaches you've tried
- Consider tracking time taken to solve (add a custom column)
- Review problems with low "Times Solved" counts periodically for practice

