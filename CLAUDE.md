# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a LeetCode practice repository organized by problem categories:

- **Arrays/** - Array manipulation problems (e.g., product except self, valid sudoku)
- **Linked-Lists/** - Linked list operations and algorithms
- **Recursion/** - Recursive algorithm implementations (fibonacci, factorial, etc.)
- **Sliding-Window/** - Sliding window technique problems
- **Stacks/** - Stack-based problems (valid parentheses, RPN evaluation)
- **Two-Pointers/** - Two-pointer technique implementations

## Code Patterns

### File Structure
Each Python file follows a consistent pattern:
- Problem description and constraints as comments at the top with emoji indicators (🧩, ✅)
- Main solution function with detailed docstring including time/space complexity
- Comprehensive test suite with multiple test cases
- `if __name__ == "__main__":` block to run tests when executed directly

### Testing Approach
- Each file includes its own test suite using Python assertions
- Test functions are named `test_<problem_name>()`
- Tests cover edge cases, examples from problem description, and additional scenarios
- Tests print success messages with checkmark emoji (✅)

### Code Style
- Type hints are used consistently (`list[int]`, `int -> int`)
- Functions include comprehensive docstrings
- Comments explain algorithmic approaches and complexity analysis
- Clean, readable variable names

## Common Commands

### Running Individual Problems
```bash
python3 <category>/<problem_file>.py
```

### Testing All Files in a Category
```bash
for file in Arrays/*.py; do echo "Testing $file" && python3 "$file"; done
```

### Finding Problems by Pattern
Use grep to search for specific algorithms or patterns:
```bash
grep -r "two.pointer" . --include="*.py"
grep -r "recursion" . --include="*.py"
```

## Development Notes

- Python 3.13.3 is the target version
- No external dependencies - uses only Python standard library
- Each solution is self-contained with its own test suite
- Focus on algorithmic correctness and efficiency over external tooling