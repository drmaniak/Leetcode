# LeetCode Practice Repository

A systematic approach to solving and tracking LeetCode problems with spaced repetition for optimal learning.

## Repository Structure

```
├── Arrays/              # Array manipulation problems
├── Binary-Search/       # Binary search algorithms
├── Linked-Lists/        # Linked list operations
├── Recursion/          # Recursive implementations
├── Sliding-Window/     # Sliding window techniques
├── Stacks/             # Stack-based problems
├── Sorting/            # Sorting algorithms
├── Two-Pointers/       # Two-pointer techniques
├── solve.py            # Problem solver & tracker
├── practice.py         # Spaced repetition selector
├── generate_tracker.py # CSV tracker generator
└── leetcode_tracker.csv # Progress tracking
```

## Quick Start

### 0. Create a problem file

> Use your favourite AI chat assistant to generate a problem skeleton and test-suite for you.
> Ensure that skeleton script matches the structure shown below.

#### File Format

Each problem file should this structure:

```python
# 🧩 Problem: Problem Name
#
# 🤔 Difficulty: Easy/Medium/Hard
# ✅ Constraints: Problem constraints...

def solution(params):
    """Solution with time/space complexity."""
    pass

def test_solution():
    """Comprehensive test cases."""
    assert solution(test_input) == expected_output
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_solution()
```

### 1. Solve a Problem

```bash
# Run and track your solution
python3 solve.py Arrays/two_sum.py

# Interactive mode for detailed tracking
python3 solve.py Arrays/two_sum.py --interactive
```

### 2. Practice Problems (Spaced Repetition)

```bash
# Select 5 problems for practice
python3 practice.py 5

# Filter by difficulty
python3 practice.py 3 --difficulty easy

# Filter by topics
python3 practice.py 5 --topics "Array,Stack"

# Balanced difficulty distribution
python3 practice.py 6 --balanced --stats
```

### 3. Generate/Update Tracker

```bash
# Create CSV tracker from all Python files
python3 generate_tracker.py
```

## Key Features

- **Automatic Tracking**: Progress logged in CSV format
- **Spaced Repetition**: Intelligent problem selection based on recency, difficulty, and frequency
- **Difficulty Detection**: Auto-extracts difficulty from file comments
- **Comprehensive Testing**: Each solution includes test suite
- **Interactive Mode**: Enhanced tracking with notes and metadata

## Commands Reference

| Command                       | Purpose                        |
| ----------------------------- | ------------------------------ |
| `python3 solve.py <file>`     | Solve and track a problem      |
| `python3 practice.py <n>`     | Select n problems for practice |
| `python3 generate_tracker.py` | Generate CSV tracker           |

## Spaced Repetition Algorithm

Problems are selected based on:

- **Recency**: Longer time since last solve = higher priority
- **Difficulty**: Hard > Medium > Easy weighting
- **Frequency**: Less frequently solved = higher priority
- **Balance**: Optional balanced difficulty distribution

Perfect for systematic LeetCode preparation and interview practice!

