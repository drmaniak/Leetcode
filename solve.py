#!/usr/bin/env python3
"""
Interactive LeetCode Solve Tracker
Executes Python problem files and automatically tracks successful solves.

Usage:
    python3 solve.py Arrays/two_sum.py           # Execute and track on success
    python3 solve.py Arrays/two_sum.py --notes   # Interactive mode with prompts
    python3 solve.py --status                    # Show recent activity
"""

import argparse
import csv
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
import shutil

TRACKER_CSV = "leetcode_tracker.csv"
BACKUP_DIR = ".tracker_backups"

def ensure_backup_dir():
    """Create backup directory if it doesn't exist."""
    os.makedirs(BACKUP_DIR, exist_ok=True)

def create_backup():
    """Create a timestamped backup of the tracker CSV."""
    if not os.path.exists(TRACKER_CSV):
        return None
    
    ensure_backup_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{BACKUP_DIR}/tracker_backup_{timestamp}.csv"
    shutil.copy2(TRACKER_CSV, backup_path)
    return backup_path

def read_tracker():
    """Read the current tracker CSV into memory."""
    if not os.path.exists(TRACKER_CSV):
        # Create empty tracker if it doesn't exist
        return []
    
    problems = []
    with open(TRACKER_CSV, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            problems.append(row)
    return problems

def write_tracker(problems):
    """Write the problems list back to the tracker CSV."""
    if not problems:
        return  # Don't create empty CSV
        
    fieldnames = ['Problem Name', 'Problem Number', 'LeetCode URL', 'Topics', 
                 'First Solved Date', 'Last Solved Date', 'Times Solved', 'Difficulty', 'Notes']
    
    with open(TRACKER_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(problems)

def extract_problem_name_from_path(file_path):
    """Extract problem name from file path."""
    filename = Path(file_path).stem
    # Convert snake_case to Title Case
    return ' '.join(word.capitalize() for word in filename.split('_'))

def find_problem_in_tracker(problems, file_path):
    """Find a problem in the tracker by file path."""
    target_name = extract_problem_name_from_path(file_path)
    
    for i, problem in enumerate(problems):
        if problem['Problem Name'] == target_name:
            return i, problem
    
    return None, None

def execute_file(file_path):
    """Execute a Python file and return success status and output."""
    try:
        # Execute the file with a timeout
        result = subprocess.run(
            [sys.executable, os.path.abspath(file_path)],
            capture_output=True,
            text=True,
            timeout=30,  # 30 second timeout
            cwd='.'  # Run from current directory
        )
        
        return result.returncode == 0, result.stdout, result.stderr
    
    except subprocess.TimeoutExpired:
        return False, "", "Execution timed out (30s limit)"
    except Exception as e:
        return False, "", f"Execution error: {str(e)}"

def extract_difficulty_from_file(file_path):
    """Extract difficulty rating from the Python file's comments."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read first 10 lines to find difficulty
            for i, line in enumerate(f):
                if i >= 10:  # Only check first 10 lines
                    break
                if '🤔 Difficulty:' in line:
                    # Extract difficulty value after the colon
                    difficulty = line.split('🤔 Difficulty:')[1].strip()
                    # Remove any comment markers
                    difficulty = difficulty.replace('#', '').strip()
                    if difficulty.lower() in ['easy', 'medium', 'hard']:
                        return difficulty.capitalize()
        return ''  # Return empty if not found
    except Exception:
        return ''  # Return empty on any error

def get_topics_from_category(file_path):
    """Extract topic category from file path."""
    topic_mappings = {
        'Arrays': 'Array',
        'Linked-Lists': 'Linked List', 
        'Two-Pointers': 'Two Pointers',
        'Stacks': 'Stack',
        'Recursion': 'Recursion',
        'Sliding-Window': 'Sliding Window',
        'Sorting': 'Sorting',
        'Binary-Search': 'Binary Search'
    }
    
    # Extract category from path like "./Arrays/problem.py"
    if '/' in file_path:
        category = file_path.split('/')[1] if file_path.startswith('./') else file_path.split('/')[0]
        return topic_mappings.get(category, category)
    return 'Misc'

def create_new_problem_entry(file_path):
    """Create a new problem entry for the tracker."""
    problem_name = extract_problem_name_from_path(file_path)
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Generate LeetCode URL (basic heuristic)
    base_name = Path(file_path).stem.replace('_', '-')
    leetcode_url = f"https://leetcode.com/problems/{base_name}/"
    
    # Extract difficulty from file
    difficulty = extract_difficulty_from_file(file_path)
    
    return {
        'Problem Name': problem_name,
        'Problem Number': '',  # Can be filled manually later
        'LeetCode URL': leetcode_url,
        'Topics': get_topics_from_category(file_path),
        'First Solved Date': today,
        'Last Solved Date': today,
        'Times Solved': '1',
        'Difficulty': difficulty,  # Auto-extracted from file
        'Notes': ''
    }

def log_solve(file_path, solve_type="practice", notes="", interactive=False):
    """Execute a problem file and log solve attempt on success."""
    
    # Validate file exists and is Python
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found.")
        return False
    
    if not file_path.endswith('.py'):
        print(f"❌ Error: File '{file_path}' is not a Python file.")
        return False
    
    print(f"🔄 Executing {file_path}...")
    
    # Execute the file
    success, stdout, stderr = execute_file(file_path)
    
    if not success:
        print(f"❌ Execution failed:")
        if stderr:
            print(f"Error: {stderr}")
        if stdout:
            print(f"Output: {stdout}")
        print("Problem not tracked due to execution failure.")
        return False
        
    print(f"✅ Execution successful!")
    if stdout:
        print(f"Output: {stdout}")
    
    # Create backup before modifying tracker
    backup_path = create_backup()
    if backup_path:
        print(f"Created backup: {backup_path}")
    
    # Read current tracker
    problems = read_tracker()
    
    # Find or create the problem entry
    problem_idx, problem = find_problem_in_tracker(problems, file_path)
    
    is_new_problem = problem is None
    
    if is_new_problem:
        # Create new problem entry
        problem = create_new_problem_entry(file_path)
        problems.append(problem)
        problem_idx = len(problems) - 1
        print(f"📝 Adding new problem to tracker: {problem['Problem Name']}")
    else:
        print(f"📝 Updating existing problem: {problem['Problem Name']}")
    
    # Interactive prompts if requested
    if interactive:
        current_times = int(problem['Times Solved']) if problem['Times Solved'] else 0
        print(f"\n📊 Problem: {problem['Problem Name']}")
        print(f"   Current times solved: {current_times}")
        print(f"   Status: {'New problem' if is_new_problem else 'Re-solve'}")
        
        # Solve type
        print("\n🏷️  Solve types:")
        print("1. initial - First time solving")
        print("2. review - Reviewing previous solution")
        print("3. optimization - Improving existing solution")
        print("4. practice - General practice/repetition")
        
        try:
            choice = input("Select solve type (1-4) [4]: ").strip()
            solve_types = {"1": "initial", "2": "review", "3": "optimization", "4": "practice"}
            solve_type = solve_types.get(choice, "practice")
            
            # Notes
            if not notes:
                notes = input("Add notes (optional): ").strip()
            
            # Difficulty (if not set, try to extract from file first)
            if not problem['Difficulty']:
                # Try to auto-extract difficulty from file
                auto_difficulty = extract_difficulty_from_file(file_path)
                if auto_difficulty:
                    print(f"Auto-detected difficulty: {auto_difficulty}")
                    problems[problem_idx]['Difficulty'] = auto_difficulty
                else:
                    difficulty = input("Set difficulty (Easy/Medium/Hard) [skip]: ").strip()
                    if difficulty.lower() in ['easy', 'medium', 'hard']:
                        problems[problem_idx]['Difficulty'] = difficulty.capitalize()
        except (EOFError, KeyboardInterrupt):
            print("\nInteractive mode cancelled, using defaults.")
            solve_type = "practice"
    
    # Update the problem entry
    today = datetime.now().strftime('%Y-%m-%d')
    current_times = int(problems[problem_idx]['Times Solved']) if problems[problem_idx]['Times Solved'] else 0
    
    if not is_new_problem:
        # For existing problems, increment counter and update date
        problems[problem_idx]['Times Solved'] = str(current_times + 1)
        problems[problem_idx]['Last Solved Date'] = today
    
    # Update notes if provided
    if notes:
        existing_notes = problems[problem_idx]['Notes']
        if existing_notes:
            problems[problem_idx]['Notes'] = f"{existing_notes}; {today}: {notes}"
        else:
            problems[problem_idx]['Notes'] = f"{today}: {notes}"
    
    # Write back to CSV
    write_tracker(problems)
    
    # Show confirmation
    new_times = int(problems[problem_idx]['Times Solved'])
    if is_new_problem:
        print(f"\n✅ New problem added and logged: {problems[problem_idx]['Problem Name']}")
        print(f"   Times solved: {new_times}")
        print(f"   Category: {problems[problem_idx]['Topics']}")
    else:
        print(f"\n✅ Re-solve logged for: {problems[problem_idx]['Problem Name']}")
        print(f"   Times solved: {current_times} → {new_times}")
    
    print(f"   Solve type: {solve_type}")
    print(f"   Date: {today}")
    if notes:
        print(f"   Notes: {notes}")
    
    return True

def show_status():
    """Show recent solving activity and stats."""
    problems = read_tracker()
    
    # Sort by last solved date
    recent_problems = sorted(problems, 
                           key=lambda x: x['Last Solved Date'] if x['Last Solved Date'] else '1900-01-01', 
                           reverse=True)
    
    print("📊 LeetCode Tracker Status")
    print("=" * 50)
    
    # Overall stats
    total_problems = len(problems)
    solved_problems = len([p for p in problems if int(p['Times Solved']) > 0])
    total_solves = sum(int(p['Times Solved']) for p in problems)
    
    print(f"Total problems tracked: {total_problems}")
    print(f"Problems solved: {solved_problems}")
    print(f"Total solve attempts: {total_solves}")
    
    # Recent activity (last 10)
    print(f"\n🕐 Recent Activity (Last 10)")
    print("-" * 50)
    
    for problem in recent_problems[:10]:
        if problem['Last Solved Date']:
            times = problem['Times Solved']
            print(f"{problem['Last Solved Date']} | {problem['Problem Name']} (×{times})")
    
    # Most practiced
    print(f"\n🔥 Most Practiced Problems")
    print("-" * 50)
    
    most_practiced = sorted(problems, key=lambda x: int(x['Times Solved']), reverse=True)
    for problem in most_practiced[:5]:
        if int(problem['Times Solved']) > 1:
            print(f"×{problem['Times Solved']} | {problem['Problem Name']}")

def main():
    parser = argparse.ArgumentParser(description="LeetCode Solve Tracker")
    parser.add_argument('file', nargs='?', help='Path to the problem file')
    parser.add_argument('--notes', action='store_true', help='Interactive mode with prompts')
    parser.add_argument('--status', action='store_true', help='Show tracker status and recent activity')
    
    args = parser.parse_args()
    
    if args.status:
        show_status()
    elif args.file:
        log_solve(args.file, interactive=args.notes)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()