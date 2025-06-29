#!/usr/bin/env python3
"""
LeetCode Problem Tracker Generator
Scans the repository and creates a CSV tracker for LeetCode problems.
"""

import csv
import os
from datetime import datetime

# Common LeetCode problem mappings (filename -> problem number)
PROBLEM_MAPPINGS = {
    "two_sum": 1,
    "valid_parentheses": 20,
    "remove_duplicates_in_sorted_array": 26,
    "remove_all_occurrences_of_number_in_place": 27,
    "first_bad_version": 278,
    "climbing_stairs": 70,
    "valid_palindrome": 125,
    "two_sum_sorted": 167,
    "reverse_linked_list": 206,
    "product_of_array_except_self": 238,
    "valid_sudoku": 36,
    "three_sum": 15,
    "container_with_most_water": 11,
    "trapping_rain_water": 42,
    "longest_substring_without_repeating": 3,
    "best_time_to_buy_sell_stock": 121,
    "longest_consecutive_sequence": 128,
    "generate_parentheses": 22,
    "swap_nodes_in_pairs": 24,
    "reverse_polish_notation": 150,
    "search_2d_matrix": 74,
    "koko_eating_bananas": 875,
    "binary_search": 704,
    # Add more mappings as needed
}


def filename_to_problem_name(filename):
    """Convert snake_case filename to Title Case problem name."""
    name = filename.replace(".py", "").replace("_", " ")
    return " ".join(word.capitalize() for word in name.split())


def get_problem_number(filename):
    """Get LeetCode problem number from filename if known."""
    base_name = filename.replace(".py", "")
    return PROBLEM_MAPPINGS.get(base_name, "")


def get_leetcode_url(problem_number, filename):
    """Generate LeetCode URL from problem number."""
    if problem_number:
        return f"https://leetcode.com/problems/{filename.replace('.py', '').replace('_', '-')}/"
    return ""


def extract_difficulty_from_file(file_path):
    """Extract difficulty rating from the Python file's comments."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Read first 10 lines to find difficulty
            for i, line in enumerate(f):
                if i >= 10:  # Only check first 10 lines
                    break
                if "🤔 Difficulty:" in line:
                    # Extract difficulty value after the colon
                    difficulty = line.split("🤔 Difficulty:")[1].strip()
                    # Remove any comment markers
                    difficulty = difficulty.replace("#", "").strip()
                    if difficulty.lower() in ["easy", "medium", "hard"]:
                        return difficulty.capitalize()
        return ""  # Return empty if not found
    except Exception:
        return ""  # Return empty on any error

def extract_leetcode_url_from_file(file_path):
    """Extract LeetCode URL from the Python file's comments."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Read first 10 lines to find LeetCode link
            for i, line in enumerate(f):
                if i >= 10:  # Only check first 10 lines
                    break
                if "🔗 Link:" in line:
                    # Extract URL after the colon
                    url = line.split("🔗 Link:")[1].strip()
                    # Remove any comment markers
                    url = url.replace("#", "").strip()
                    # Basic URL validation
                    if url.startswith("https://leetcode.com/"):
                        return url
        return ""  # Return empty if not found
    except Exception:
        return ""  # Return empty on any error


def get_topics_from_category(category):
    """Map directory category to topics."""
    topic_mappings = {
        "Arrays": "Array",
        "Linked-Lists": "Linked List",
        "Two-Pointers": "Two Pointers",
        "Stacks": "Stack",
        "Recursion": "Recursion",
        "Sliding-Window": "Sliding Window",
        "Sorting": "Sorting",
        "Binary-Search": "Binary Search",
    }
    return topic_mappings.get(category, category)


def main():
    """Generate the LeetCode tracker CSV."""
    # Get all Python files and their metadata
    file_data = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and file != "generate_tracker.py":
                file_path = os.path.join(root, file)
                stat = os.stat(file_path)

                # Extract category from path
                # File path is like "./Arrays/filename.py"
                if "/" in file_path:
                    category = file_path.split("/")[1]
                else:
                    category = "Misc"

                file_data.append(
                    {
                        "filepath": file_path,
                        "filename": file,
                        "category": category,
                        "created": stat.st_ctime,
                        "modified": stat.st_mtime,
                    }
                )

    # Create CSV data
    csv_data = []
    for file_info in file_data:
        filename = file_info["filename"]
        base_name = filename.replace(".py", "")

        problem_name = filename_to_problem_name(filename)
        problem_number = get_problem_number(filename)
        
        # Extract LeetCode URL from file, fallback to existing logic
        leetcode_url = extract_leetcode_url_from_file(file_info["filepath"])
        if not leetcode_url:
            # Fallback to existing URL generation logic
            leetcode_url = (
                get_leetcode_url(problem_number, filename)
                if problem_number
                else f"https://leetcode.com/problems/{base_name.replace('_', '-')}/"
            )
        
        topics = get_topics_from_category(file_info["category"])
        first_solved = datetime.fromtimestamp(file_info["created"]).strftime("%Y-%m-%d")
        last_solved = datetime.fromtimestamp(file_info["modified"]).strftime("%Y-%m-%d")

        # Extract difficulty from file
        difficulty = extract_difficulty_from_file(file_info["filepath"])

        csv_data.append(
            {
                "Problem Name": problem_name,
                "Problem Number": problem_number,
                "LeetCode URL": leetcode_url,
                "Topics": topics,
                "First Solved Date": first_solved,
                "Last Solved Date": last_solved,
                "Times Solved": 1,  # Default to 1, user can update manually
                "Difficulty": difficulty,  # Auto-extracted from file
                "Notes": "",  # User can add notes
            }
        )

    # Sort by problem number (if available), then by name
    csv_data.sort(key=lambda x: (x["Problem Number"] or 9999, x["Problem Name"]))

    # Write to CSV
    with open("leetcode_tracker.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "Problem Name",
            "Problem Number",
            "LeetCode URL",
            "Topics",
            "First Solved Date",
            "Last Solved Date",
            "Times Solved",
            "Difficulty",
            "Notes",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(csv_data)

    print(f"Generated leetcode_tracker.csv with {len(csv_data)} problems")
    print("CSV Schema:")
    print("- Problem Name: Human-readable problem name")
    print("- Problem Number: LeetCode problem number (if known)")
    print("- LeetCode URL: Direct link to the problem")
    print("- Topics: Problem categories/topics")
    print("- First Solved Date: Date when first solved")
    print("- Last Solved Date: Most recent solve date")
    print("- Times Solved: Counter for number of attempts (manually updated)")
    print("- Difficulty: Easy/Medium/Hard (manually filled)")
    print("- Notes: Personal notes about the problem")


if __name__ == "__main__":
    main()

