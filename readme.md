# Homework 3

## Task: Run Static Analysis Tools

Add package to dependencies:

- [x] pylint (general static analysis and code quality)
- [x] pyflakes (error detection)
- [x] bandit (security vulnerabilities)
- [ ] radon (complexity analysis)


## Task: Create your own branch

1. Add extra code (any algorithm with issues; the algorithm should be different from your group members’). It is recommended that students implement the algorithm by hand rather than copying an example online. This approach will help reinforce the understanding of debugging techniques, which are key learning objectives of this assignment.

2. Run tools on all files:
```bash
pylint hw2_debugging.py rand.py > pylint_report.txt
pyflakes hw2_debugging.py rand.py > pyflakes_report.txt
```

3. Fix issues reported by static analysis
   - Correct coding style violations, security concerns, and potential logical errors.
   - Ensure that all fixes maintain the intended functionality.

4. Re-run the Tools: After fixing issues, rerun each tool and save the updated results inside a post_traces folder.
5. After fixing the code, commit changes to your repository.

Task done by:

- [ ] `zgong6`
- [ ] `azkuang2`
- [ ] `opdesai2`

## Task: Write 3 test cases for merge sort using pytest

Task done by:

- [x] `zgong6` added pytest for [`None` input](tests/test_none_input.py), [empty list](tests/test_empty_input.py), and a [list with one element](tests/test_single_element_input.py)
- [ ] `azkuang2`
- [ ] `opdesai2`

## Task: Merge all branches

## Task: Configure automated testing to run on every commit

- [ ] Assigned to @visualDust