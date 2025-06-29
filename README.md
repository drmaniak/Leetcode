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

### For New Users (First Time Setup)

If you're starting fresh with no existing problems:

```bash
# 1. Create your first problem file in appropriate directory
# 2. Run generate_tracker.py to create initial CSV
python3 generate_tracker.py

# 3. Start your regular practice workflow
python3 practice.py 5
```

### Regular Workflow (Daily Use)

#### 1. Create a Problem File

> Use your favourite AI chat assistant to generate a problem skeleton and test-suite for you.
> Ensure that skeleton script matches the structure shown below.

Each problem file should follow this structure:

```python
# 🧩 Problem: Problem Name
#
# 🤔 Difficulty: Easy/Medium/Hard
#
# 🔗 Link: https://leetcode.com/problems/problem-name
#
#   <Description>...
#
# ✅ Constraints: Problem constraints...

def solution(params): # Solution and tester functions can be named as per your choice
    """Solution with time/space complexity."""
    pass

def test_solution():
    """Comprehensive test cases."""
    assert solution(test_input) == expected_output
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_solution()
```

#### 2. Solve a Problem

```bash
# Run and automatically track your solution
python3 solve.py Arrays/two_sum.py

# Interactive mode for detailed tracking with notes
python3 solve.py Arrays/two_sum.py --interactive
```

**Note**: `solve.py` automatically creates CSV entries for new problems and updates existing ones.

#### 3. Practice Problems (Spaced Repetition)

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

## Key Features

- **Automatic Tracking**: Progress logged in CSV format
- **Spaced Repetition**: Intelligent problem selection based on recency, difficulty, and frequency
- **Difficulty Detection**: Auto-extracts difficulty from file comments
- **Comprehensive Testing**: Each solution includes test suite
- **Interactive Mode**: Enhanced tracking with notes and metadata

## Commands Reference

| Command                       | Purpose                        | When to Use                                   |
| ----------------------------- | ------------------------------ | --------------------------------------------- |
| `python3 solve.py <file>`     | Solve and track a problem      | **Daily use** - Run after solving any problem |
| `python3 practice.py <n>`     | Select n problems for practice | **Daily use** - Choose problems to re-solve   |
| `python3 generate_tracker.py` | Generate CSV from all files    | **Setup only** - First time or bulk import    |

## Advanced Use Cases

### Bulk Import Existing Problems

```bash
# If you have many existing problem files without tracking
python3 generate_tracker.py
```

### Recovery from CSV Loss

```bash
# Recreate tracker from existing files
python3 generate_tracker.py
```

### View Tracking Status

```bash
# See recent activity and statistics
python3 solve.py --status
```

## Spaced Repetition Algorithm

Problems are selected based on:

- **Recency**: Longer time since last solve = higher priority
- **Difficulty**: Hard > Medium > Easy weighting
- **Frequency**: Less frequently solved = higher priority
- **Balance**: Optional balanced difficulty distribution
