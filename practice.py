#!/usr/bin/env python3
"""
LeetCode Practice Problem Selector with Spaced Repetition
Intelligently selects problems for practice based on recency, difficulty, and frequency.

Usage:
    python3 practice.py 5                    # Select 5 problems
    python3 practice.py 3 --easy             # Select 3 easy problems only
    python3 practice.py 10 --topics Array,Stack  # Filter by topics
    python3 practice.py 5 --min-days 7       # Only problems not solved in 7+ days
    python3 practice.py 5 --balanced         # Ensure balanced difficulty distribution
"""

import argparse
import csv
import math
import os
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

TRACKER_CSV = "leetcode_tracker.csv"

def read_tracker() -> List[Dict]:
    """Read the tracker CSV and return list of problems."""
    if not os.path.exists(TRACKER_CSV):
        print(f"❌ Error: {TRACKER_CSV} not found. Run generate_tracker.py first.")
        return []
    
    problems = []
    with open(TRACKER_CSV, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Problem Name']:  # Skip empty rows
                problems.append(row)
    return problems

def days_since_last_solve(last_solved_date: str) -> int:
    """Calculate days since last solve date."""
    if not last_solved_date:
        return 365  # Default to 1 year if no date
    
    try:
        last_date = datetime.strptime(last_solved_date, '%Y-%m-%d')
        today = datetime.now()
        return (today - last_date).days
    except ValueError:
        return 365  # Default if date parsing fails

def calculate_priority_score(problem: Dict) -> float:
    """
    Calculate priority score for spaced repetition.
    Higher score = higher priority for practice.
    
    Factors:
    - Recency: Exponential increase based on days since last solve
    - Difficulty: Hard > Medium > Easy multiplier
    - Frequency: Logarithmic penalty for frequently solved problems
    """
    # Recency factor (exponential growth)
    days_ago = days_since_last_solve(problem['Last Solved Date'])
    recency_score = math.exp(days_ago / 30.0)  # Exponential with 30-day half-life
    
    # Difficulty multiplier
    difficulty = problem.get('Difficulty', '').lower()
    difficulty_multipliers = {
        'hard': 1.5,
        'medium': 1.2,
        'easy': 1.0
    }
    difficulty_multiplier = difficulty_multipliers.get(difficulty, 1.0)
    
    # Frequency penalty (logarithmic)
    times_solved = int(problem.get('Times Solved', 1))
    frequency_penalty = 1.0 / math.log(times_solved + 1)  # +1 to avoid log(0)
    
    # Base randomness to avoid always selecting same problems
    randomness = random.uniform(0.8, 1.2)
    
    priority_score = recency_score * difficulty_multiplier * frequency_penalty * randomness
    
    return priority_score

def find_problem_file(problem_name: str) -> Optional[str]:
    """Find the corresponding Python file for a problem."""
    # Convert problem name to snake_case filename
    snake_case = problem_name.lower().replace(' ', '_').replace('-', '_')
    
    # Search in all subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                file_stem = Path(file).stem
                if file_stem == snake_case:
                    return os.path.join(root, file)
    
    return None

def filter_problems(problems: List[Dict], 
                   difficulty: Optional[str] = None,
                   topics: Optional[List[str]] = None,
                   min_days: Optional[int] = None) -> List[Dict]:
    """Filter problems based on criteria."""
    filtered = problems.copy()
    
    # Filter by difficulty
    if difficulty:
        filtered = [p for p in filtered if p.get('Difficulty', '').lower() == difficulty.lower()]
    
    # Filter by topics
    if topics:
        filtered = [p for p in filtered if any(topic.lower() in p.get('Topics', '').lower() for topic in topics)]
    
    # Filter by minimum days since last solve
    if min_days:
        filtered = [p for p in filtered if days_since_last_solve(p['Last Solved Date']) >= min_days]
    
    return filtered

def ensure_balanced_selection(problems: List[Dict], n: int) -> List[Dict]:
    """Ensure balanced selection across difficulties if possible."""
    if len(problems) <= n:
        return problems
    
    # Group by difficulty
    by_difficulty = {'Easy': [], 'Medium': [], 'Hard': []}
    for problem in problems:
        difficulty = problem.get('Difficulty', 'Medium').capitalize()
        if difficulty in by_difficulty:
            by_difficulty[difficulty].append(problem)
    
    # Calculate target distribution (roughly 40% Easy, 40% Medium, 20% Hard)
    targets = {
        'Easy': max(1, int(n * 0.4)),
        'Medium': max(1, int(n * 0.4)),
        'Hard': max(1, int(n * 0.2))
    }
    
    # Adjust targets based on available problems
    total_available = sum(len(probs) for probs in by_difficulty.values())
    if total_available < n:
        n = total_available
    
    selected = []
    remaining = n
    
    # Select from each difficulty level
    for difficulty, target in targets.items():
        available = by_difficulty[difficulty]
        if available and remaining > 0:
            take = min(target, len(available), remaining)
            # Sort by priority and take top ones
            available.sort(key=calculate_priority_score, reverse=True)
            selected.extend(available[:take])
            remaining -= take
    
    # Fill remaining slots with highest priority problems
    if remaining > 0:
        all_remaining = [p for p in problems if p not in selected]
        all_remaining.sort(key=calculate_priority_score, reverse=True)
        selected.extend(all_remaining[:remaining])
    
    return selected

def select_practice_problems(n: int, 
                           difficulty: Optional[str] = None,
                           topics: Optional[List[str]] = None,
                           min_days: Optional[int] = None,
                           balanced: bool = False) -> List[Dict]:
    """Select n problems for practice using spaced repetition algorithm."""
    problems = read_tracker()
    if not problems:
        return []
    
    # Filter problems based on criteria
    filtered_problems = filter_problems(problems, difficulty, topics, min_days)
    
    if not filtered_problems:
        print("❌ No problems match the specified criteria.")
        return []
    
    # Calculate priority scores
    for problem in filtered_problems:
        problem['_priority_score'] = calculate_priority_score(problem)
    
    # Select problems
    if balanced:
        selected = ensure_balanced_selection(filtered_problems, n)
    else:
        # Sort by priority score and take top n
        filtered_problems.sort(key=lambda p: p['_priority_score'], reverse=True)
        selected = filtered_problems[:n]
    
    return selected

def display_selected_problems(problems: List[Dict]):
    """Display selected problems with their details and commands."""
    if not problems:
        print("No problems selected.")
        return
    
    print(f"\n🎯 Selected {len(problems)} problems for practice:")
    print("=" * 80)
    
    for i, problem in enumerate(problems, 1):
        # Find corresponding file
        file_path = find_problem_file(problem['Problem Name'])
        
        # Calculate display info
        days_ago = days_since_last_solve(problem['Last Solved Date'])
        times_solved = problem.get('Times Solved', '1')
        difficulty = problem.get('Difficulty', 'Unknown')
        topics = problem.get('Topics', 'Unknown')
        priority = problem.get('_priority_score', 0)
        
        print(f"\n{i}. {problem['Problem Name']}")
        print(f"   📊 Difficulty: {difficulty} | Topics: {topics}")
        print(f"   📅 Last solved: {days_ago} days ago | Times solved: {times_solved}")
        print(f"   🎯 Priority score: {priority:.2f}")
        
        if file_path:
            print(f"   📁 File: {file_path}")
            print(f"   ▶️  Command: python3 solve.py {file_path}")
        else:
            print(f"   ❌ File not found for this problem")
        
        print(f"   🔗 URL: {problem.get('LeetCode URL', 'N/A')}")

def show_stats(problems: List[Dict]):
    """Show statistics about the problem set."""
    if not problems:
        return
    
    print(f"\n📈 Practice Session Statistics:")
    print("-" * 40)
    
    # Difficulty distribution
    difficulties = {}
    for problem in problems:
        diff = problem.get('Difficulty', 'Unknown')
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    print("Difficulty distribution:")
    for diff, count in sorted(difficulties.items()):
        print(f"  {diff}: {count}")
    
    # Topic distribution
    topics = {}
    for problem in problems:
        topic = problem.get('Topics', 'Unknown')
        topics[topic] = topics.get(topic, 0) + 1
    
    if len(topics) <= 8:  # Only show if not too many topics
        print("\nTopic distribution:")
        for topic, count in sorted(topics.items()):
            print(f"  {topic}: {count}")
    
    # Average days since last solve
    avg_days = sum(days_since_last_solve(p['Last Solved Date']) for p in problems) / len(problems)
    print(f"\nAverage days since last solve: {avg_days:.1f}")

def main():
    parser = argparse.ArgumentParser(description="LeetCode Practice Problem Selector")
    parser.add_argument('count', type=int, help='Number of problems to select')
    parser.add_argument('--difficulty', choices=['easy', 'medium', 'hard'], 
                       help='Filter by difficulty level')
    parser.add_argument('--topics', help='Filter by topics (comma-separated)')
    parser.add_argument('--min-days', type=int, 
                       help='Minimum days since last solve')
    parser.add_argument('--balanced', action='store_true',
                       help='Ensure balanced difficulty distribution')
    parser.add_argument('--stats', action='store_true',
                       help='Show statistics about selected problems')
    
    args = parser.parse_args()
    
    # Parse topics
    topics = None
    if args.topics:
        topics = [t.strip() for t in args.topics.split(',')]
    
    # Select problems
    selected_problems = select_practice_problems(
        n=args.count,
        difficulty=args.difficulty,
        topics=topics,
        min_days=args.min_days,
        balanced=args.balanced
    )
    
    # Display results
    display_selected_problems(selected_problems)
    
    if args.stats and selected_problems:
        show_stats(selected_problems)
    
    if selected_problems:
        print(f"\n💡 Tip: Use 'python3 solve.py <file_path>' to practice each problem")
        print(f"📝 Your progress will be automatically tracked!")

if __name__ == "__main__":
    main()