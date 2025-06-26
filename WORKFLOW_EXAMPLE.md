# LeetCode Workflow Example

## Your New Streamlined Workflow

Here's how your LeetCode practice workflow now works:

### 1. Create and Solve a Problem
```bash
# Create your problem file
vim Binary-Search/find_minimum_in_rotated_sorted_array.py

# Implement your solution with tests
# (following your existing pattern with test functions)
```

### 2. Execute and Track Automatically  
```bash
# Run this when you've solved the problem
python3 solve.py Binary-Search/find_minimum_in_rotated_sorted_array.py
```

**What happens:**
- ✅ Executes your Python file
- ✅ If tests pass → Adds new problem to tracker (times solved = 1)
- ✅ If tests fail → Shows error, doesn't track anything
- ✅ Creates automatic backup before any changes

### 3. Re-solve Later (Optional)
```bash
# When you want to practice the problem again
python3 solve.py Binary-Search/find_minimum_in_rotated_sorted_array.py
```

**What happens:**
- ✅ Executes your Python file again
- ✅ If tests pass → Increments counter (1 → 2) and updates date
- ✅ If tests fail → Shows error, doesn't update anything

### 4. Track Your Progress
```bash
# View your progress anytime
python3 solve.py --status
```

## Key Benefits

1. **No manual CSV editing** - Everything is automatic
2. **Quality assurance** - Only working solutions get tracked
3. **Data safety** - Automatic backups protect your progress
4. **Zero overhead** - Just solve and run, that's it!

## Example Session

```bash
# Day 1: Solve a new problem
vim Arrays/container_with_most_water.py
# ... implement solution ...
python3 solve.py Arrays/container_with_most_water.py
# ✅ New problem added and logged: Container With Most Water
#    Times solved: 1

# Day 5: Practice the same problem with optimization
vim Arrays/container_with_most_water.py
# ... try different approach ...
python3 solve.py Arrays/container_with_most_water.py  
# ✅ Re-solve logged for: Container With Most Water
#    Times solved: 1 → 2

# Check your progress
python3 solve.py --status
# 📊 Shows recent activity and most practiced problems
```

This workflow eliminates the need to run `generate_tracker.py` and manually update counters - everything just works!